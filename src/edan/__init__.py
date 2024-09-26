#!/usr/bin/env python3
#
# Search metadata in the EDAN API
# v 0.4
# 

import urllib.parse
import urllib.request
import time
import uuid
import hashlib
import json
from base64 import b64encode

# For testing
from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError


def query_edan(edan_q, url, AppID=None, AppKey=None):
    """
    Execute the query
    """
    # Date of request
    RequestDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # Nonce generated uniquely for this request
    #   using UUIDv4
    Nonce = uuid.uuid4().hex
    # This will be the value of X-AuthContent, each element is joined by a single newline
    StringToSign = "{}\n{}\n{}\n{}".format(Nonce, edan_q, RequestDate, AppKey)
    # Hash using SHA1
    HashedString = hashlib.sha1(StringToSign.encode('utf-8')).hexdigest()
    # Base64 encode
    EncodedString = b64encode(HashedString.encode('utf-8')).decode('utf-8')
    # Set headers
    headers = {'X-AppId': AppID, 'X-Nonce': Nonce, 'X-RequestDate': RequestDate, 'X-AuthContent': EncodedString}
    # Make request
    req = urllib.request.Request(url=url, headers=headers, method="GET")
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error: {} ({})'.format(e.reason, e.code))
        return False
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
        return False
    else:
        data = response.read().decode('utf-8')
        return json.loads(data)


def content_getcontent(id=None, url=None, AppID=None, AppKey=None):
    """
    Get details from an item using an EDAN ID or url
    """
    if AppID is None:
        raise ValueError("Missing AppID")
    if AppKey is None:
        raise ValueError("Missing AppKey")
    if id is None and url is None:
        raise ValueError("id or url is missing")
    if id is not None and url is not None:
        raise ValueError("Use id or url, not both")
    # Request
    if id != None:
        edan_q = "id={}".format(id)
    elif url != None:
        edan_q = "url={}".format(url)
    # Put whole thing together
    url = 'https://edan.si.edu/content/v2.0/content/getContent.htm?{}'.format(edan_q)
    # Execute query
    result = query_edan(edan_q, url, AppID, AppKey)
    return result


def metadata_search(q=None, fqs=[], edan_schema=None, AppID=None, AppKey=None, rows=10, start=0):
    """
    Returns the results of the search in JSON.
    """
    if AppID is None:
        raise ValueError("Missing AppID")
    if AppKey is None:
        raise ValueError("Missing AppKey")
    # Request
    if q is None and fqs is None:
        raise ValueError("Missing q or fqs")
    if q is None:
        edan_query = "q=*:*"
    else:
        edan_query = urllib.parse.quote_plus("q={}".format(q))
    edan_schema_vals = ["3d_package","damsmdm","ead_collection","ead_component","ecr","edanlists","edanmdm","emammal_image","event","location","objectgroup","objectlists","page","si-unit","transproject","transasset"]
    if fqs != [] or edan_schema_vals is not None:
        if isinstance(fqs, list) == False:
            raise ValueError("fqs needs to be type list")
        else:
            if edan_schema is not None:
                if edan_schema not in edan_schema_vals:
                    raise ValueError("edan_schema is not valid")
                fqs.append("type:{}".format(edan_schema))
            fqs_query = json.dumps(fqs)
            # fqs_query = urllib.parse.quote_plus(fqs_query)
            fqs_query = fqs_query.replace(" ", "+")
    else:
        fqs_query = ""
    edan_q = "{}&fqs={}&rows={}&start={}&facet=true".format(edan_query, fqs_query, rows, start)
    # Put whole thing together
    url = 'https://edan.si.edu/metadata/v2.0/metadata/search.htm?{}'.format(edan_q)
    # Execute query
    result = query_edan(edan_q, url, AppID, AppKey)
    return result


def metadata_suggestions(suggest=None, AppID=None, AppKey=None):
    """
    Returns a list of suggested content for a given search term.
    """
    if suggest is None:
        raise ValueError("Missing suggest")
    if AppID is None:
        raise ValueError("Missing AppID")
    if AppKey is None:
        raise ValueError("Missing AppKey")
    # Request
    edan_query = urllib.parse.quote_plus(suggest)
    edan_q = "suggest={}".format(edan_query)
    # Put whole thing together
    url = 'https://edan.si.edu/metadata/v2.0/metadata/getSuggestions.htm?{}'.format(edan_q)
    # Execute query
    result = query_edan(edan_q, url, AppID, AppKey)
    return result['suggestions']


# To test and add later
# 
# def edan_metadata_getFacets(edan_query, AppID=None, AppKey=None, limit=100, mincount=1, offset=0, sort="index"):
#     """
#     Returns facets found for a given search term. All requests will timeout after 30 seconds and may return incomplete results; measuring performance is required before implementing in a production environment.
#     """
#     if AppID is None:
#         raise ValueError("Missing AppID")
#     if AppKey is None:
#         raise ValueError("Missing AppKey")
#     # Request
#     edan_query = urllib.parse.quote_plus(edan_query)
#     edan_q = "q={}&limit={}&mincount={}&offset={}&sort={}".format(edan_query, limit, mincount, offset, sort)
#     # Put whole thing together
#     url = 'https://edan.si.edu/metadata/v2.0/metadata/getFacets.htm?{}'.format(edan_q)
#     # Execute query
#     result = query_edan(edan_q, url, AppID, AppKey)
#     return result

