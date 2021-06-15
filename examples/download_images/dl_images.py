#!/usr/bin/env python3
#
# Download images in a file with their EDAN id
#

import edan, json, wget
from pathlib import Path
import settings

with open('images.txt') as f:
    files_list = f.read().splitlines()


for file in files_list:
    print('Downloading {}...'.format(file))

    #Search for images of orchids from Smithsonian Gardens
    results = edan.searchEDAN(file, settings.AppID, settings.AppKey)

    #Number of results available for this search
    if results['rowCount'] == 1:

        media_files_count = results['rows'][0]['content']['descriptiveNonRepeating']['online_media']['mediaCount']
        if media_files_count > 0:
            for i in range(0, media_files_count):
                idsID = results['rows'][0]['content']['descriptiveNonRepeating']['online_media']['media'][i]['idsId']
                #Found image with full link
                if idsID[:4] == "http":
                    wget.download(idsID, 'images/{}'.format(Path(idsID).name))
                    break
                else:
                    wget.download("https://ids.si.edu/ids/deliveryService?id={}".format(idsID), 'images/{}.jpg'.format(idsID))
                    break
    print('\n')
