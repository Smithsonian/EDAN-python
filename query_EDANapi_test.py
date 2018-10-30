#!/usr/bin/python3
#
# Test for the EDAN API

import urllib.parse
import urllib.request
import datetime
import email.utils
import uuid
import hashlib
from base64 import b64encode

#for testing
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError




import settings
#settings.py should contain:
#   AppID = ""
#   AppKey = ""
#   API_url = ""


#Authentication based on brief example at
#  https://edandoc.si.edu/authentication


#Date of request
dt = datetime.datetime.now()
RequestDate = email.utils.format_datetime(dt)

#Generated uniquely for this request
Nonce = str(uuid.uuid4()).replace('-', '')
	
#Your request (example of format to enter query parameters)
QueryParameters = "q=orchids&rows=10&start=0&facet=true"

#This will be the value of X-AuthContent, each element is joined by a single newline
StringToSign = "{}\n{}\n{}\n{}".format(Nonce, QueryParameters, RequestDate, settings.AppKey)

#First hash using SHA1
HashedString = hashlib.sha1(StringToSign.encode('utf-8')).hexdigest()

#Base64 encode
EncodedString = b64encode(HashedString.encode('utf-8')).decode('utf-8')

#API url
url = '{}metadata/v2.0/collections/search.htm?{}'.format(settings.API_url, QueryParameters)

#To add: Convert QueryParameters to json here
# values = {}
# vals = QueryParameters.split('&')
# for i in range(0,len(vals)):
# 	keypair = vals[i].split('=')
# 	values[keypair[0]] = keypair[1]

# values = json.dumps(values)
values = {'id': 'edanmdm-chndm_1896-31-49'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

#Set headers
headers = {'X-AppId': settings.AppID, 'X-Nonce': Nonce, 'X-RequestDate': RequestDate, 'X-AuthContent': EncodedString}

#Make request
#req = urllib.request.Request(url, data, headers)
req = urllib.request.Request(url = url, headers = headers, method = "GET")

#test if it works
try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
	json = response.read()


#Print results
print(json)
