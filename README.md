![EDAN API](https://badgen.net/static/EDAN%20API/up/green)

# EDAN python

Basic python3 module to query the Smithsonian's Enterprise Digital Asset Network (EDAN). Requires Python 3.11 or higher.

## Installation

Install using pip:

```bash
pip install edan
```

Then, load the module:

```python
import edan
```

## Search EDAN

Set your credentials and use `edan.edan_metadata_search()`:

```python
#EDAN creds
AppID = "APP_ID"
AppKey = "verylong_key"

#Search for images of orchids from Smithsonian Gardens
results = edan.edan_metadata_search("orchids smithsonian gardens images", AppID=AppID, AppKey=AppKey)

#Number of results available for this search
results['rowCount']

#To get the rows of results
results_rows = results['rows']
```

The function `edan_metadata_search()` takes these arguments:

 * edan_query = Search items
 * fqs = JSON array of filter query parameters
 * AppID = Your AppID
 * AppKey = Your AppKey
 * rows = How many rows to return, max is 100, default is 10
 * start = Which row to start the results, default is 0

## Get details of a single item using the item ID

```python
import json

item = edan.edan_content_getcontent(results['rows'][0]['url'], AppID=AppID, AppKey=AppKey)
```

The function `edan_content_getcontent()` takes these arguments (must provide `id` or `url`):

 * id = ID of the item
 * id = URL of the item
 * AppID = Your AppID
 * AppKey = Your AppKey
 
To see the details of the item:

```python
print(json.dumps(item, sort_keys = True, indent = 4))
```
