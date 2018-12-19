# EDAN python

Basic python3 module to query the Smithsonian's Enterprise Digital Asset Network (EDAN).

## Load the module

Save the file `edan.py` and load it as a module:

```python
import edan
```

## Search EDAN

Search EDAN:

```python
#EDAN creds
AppID = "APP_ID"
AppKey = "verylong_key"

#Search for images of orchids from Smithsonian Gardens
results = edan.searchEDAN("orchids smithsonian gardens images", AppID, AppKey)

#Number of results available for this search
results['rowCount']

#To get the rows of results
results_rows = results['rows']
```

## Get details of a single item using the item ID

```python
import json

item = edan.getContentEDAN(results['rows'][0]['url'], AppID, AppKey)

print(json.dumps(item, sort_keys = True, indent = 4))
```

Returns:

```json
{
    "content": {
        "descriptiveNonRepeating": {
            "data_source": "Smithsonian Gardens",
            "online_media": {
                "media": [
                    {
                        "caption": "Photographed by: Creekside Digital",
                        "content": "http://ids.si.edu/ids/deliveryService?id=OFEO-SG-2012-1080A-101",
                        "idsId": "OFEO-SG-2012-1080A-101",
                        "thumbnail": "http://ids.si.edu/ids/deliveryService?id=OFEO-SG-2012-1080A-101",
                        "type": "Images"
                    },
                    {
                        "caption": "Photographed by: Creekside Digital",
                        "content": "http://ids.si.edu/ids/deliveryService?id=OFEO-SG-2012-1080A-102",
                        "idsId": "OFEO-SG-2012-1080A-102",
                        "thumbnail": "http://ids.si.edu/ids/deliveryService?id=OFEO-SG-2012-1080A-102",
                        "type": "Images"
                    }
                ],
                "mediaCount": "2"
            },
            "record_ID": "ofeo-sg_2012-1080A",
            "title": {
                "content": "Rhyncholaeliocattleya Lise Calov 'Exotic Orchids'",
                "label": "Title"
            },
            "title_sort": "RHYNCHOLAELIOCATTLEYA LISE CALOV 'EXOTIC ORCHIDS'",
            "unit_code": "OFEO-SG"
        },
        "freetext": {
            "dataSource": [
                {
                    "content": "Smithsonian Gardens",
                    "label": "Data Source"
                }
            ],
            "identifier": [
                {
                    "content": "2012-1080A",
                    "label": "Accession Number"
                }
            ],
            "notes": [
                {
                    "content": "Rhyncholaeliocattleya Memoria Seichi Iwasaki x Cattleya Beaufort",
                    "label": "Parentage"
                },
                {
                    "content": "From a cultivated plant not of known wild origin",
                    "label": "Provenance"
                }
            ],
            "physicalDescription": [
                {
                    "content": "Orange; Red center",
                    "label": "Flower Color"
                }
            ],
            "setName": [
                {
                    "content": "Smithsonian Gardens Orchid Collection",
                    "label": "See more items in"
                }
            ],
            "taxonomicName": [
                {
                    "content": "[vascular plants]",
                    "label": "Group"
                },
                {
                    "content": "Equisetopsida",
                    "label": "Class"
                },
                {
                    "content": "Magnoliidae",
                    "label": "Subclass"
                },
                {
                    "content": "Lilianae",
                    "label": "Superorder"
                },
                {
                    "content": "Asparagales",
                    "label": "Order"
                },
                {
                    "content": "Orchidaceae",
                    "label": "Family"
                },
                {
                    "content": "Rhyncholaeliocattleya",
                    "label": "Genus"
                }
            ],
            "topic": [
                {
                    "content": "Orchids",
                    "label": "Topic"
                }
            ]
        },
        "indexedStructured": {
            "object_type": [
                "Living botanical specimens"
            ],
            "online_media_type": [
                "Images"
            ],
            "scientific_name": [
                "Rhyncholaeliocattleya"
            ],
            "tax_class": [
                "Equisetopsida"
            ],
            "tax_family": [
                "Orchidaceae"
            ],
            "tax_order": [
                "Asparagales"
            ],
            "topic": [
                "Orchids",
                "Plants"
            ]
        }
    },
    "docSignature": "99c4fa09ec3f8e8d82ba161049cb1fc5780e8868_671f3a7646fc99059836c5767ce99aa1",
    "hash": "99c4fa09ec3f8e8d82ba161049cb1fc5780e8868",
    "id": "edanmdm-ofeo-sg_2012-1080A",
    "lastTimeUpdated": "Fri May 25 04:22:36 EDT 2018",
    "linkedContent": [],
    "linkedId": "0",
    "publicSearch": true,
    "status": 0,
    "timestamp": "Fri May 25 04:22:36 EDT 2018",
    "title": "Rhyncholaeliocattleya Lise Calov 'Exotic Orchids'",
    "type": "edanmdm",
    "unitCode": "OFEO-SG",
    "url": "edanmdm:ofeo-sg_2012-1080A",
    "version": ""
}
```
