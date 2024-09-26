# EDAN python

Basic python3 module to query the Smithsonian's Enterprise Digital Asset Network (EDAN). Requires Python 3.11 or higher.

## Installation

Install using pip:

```bash
pip install edan
```

Then, load the module in Python:

```python
import edan
```

You will need an ID and key, make the request in ServiceNow: https://edandoc.si.edu/more.html#auth

## metadata_search() - Search EDAN

The function `metadata_search()` takes these arguments:

 * `q` = Search terms
 * `fqs` = Python list of filter query parameters, for example:
   * `["online_media_type:\"Images\""]` - Select records with images
   * `["data_source:\"Smithsonian+Gardens\""]` - Limit results to a unit, SG in this case 
 * `edan_schema` = Filter results by specifying one of the valid EDAN schemas or record types (list at https://edandoc.si.edu/more.html#schemas)
 * `AppID` = Your AppID
 * `AppKey` = Your AppKey
 * `rows` = How many rows to return, max is 100, default is 10
 * `start` = Which row to start the results, default is 0

Example of setting your credentials and using `metadata_search()`:

```python
#EDAN creds
AppID = "APP_ID"
AppKey = "verylong_key"

#Search for images of orchids from Smithsonian Gardens
results = edan.metadata_search(q="orchids", fqs=["online_media_type:\"Images\"", "data_source:\"Smithsonian+Gardens\""],  AppID=AppID, AppKey=AppKey)

#Number of results available for this search
results['rowCount']

#To get the rows of results
results_rows = results['rows']
```

To get the list of units: 

```python
unit_search = edan.metadata_search(edan_schema="si-unit", AppID=AppID, AppKey=AppKey, rows=100)

# Create a list with unit title, url in EDAN, and description
units = []

#iterate through the results and save to list
for i in range(len(unit_search['rows'])):
    units.append([unit_search['rows'][i]['title'], unit_search['rows'][i]['url'], unit_search['rows'][i]['content']['description']])
```

## content_getcontent() - Get details of a single item using the item ID

The function `content_getcontent()` takes these arguments (must provide either `id` or `url`):

 * `id` = ID of the item
 * `url` = URL of the item
 * `AppID` = Your AppID
 * `AppKey` = Your AppKey

To see the details of an item:

```python
import json

item = edan.content_getcontent(url=results['rows'][0]['url'], AppID=AppID, AppKey=AppKey)

print(json.dumps(item, sort_keys = True, indent = 4))
```


## metadata_suggestions() - Returns a list of suggested content for a given search term

The function `metadata_suggestions()` takes these arguments:

 * `suggest` = Search terms
 * `AppID` = Your AppID
 * `AppKey` = Your AppKey