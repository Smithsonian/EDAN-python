#!/usr/bin/env python3
#

import edan
import time
import pandas as pd
import settings
import math
from tqdm import tqdm

# # Parallel
# import multiprocessing
# from p_tqdm import p_map

# no_workers = (multiprocessing.cpu_count()) - 1

# Get number of rows in result
results = edan.metadata_search(edan_schema="transproject", AppID=settings.AppID, AppKey=settings.AppKey, rows=1)
no_rows = results['rowCount']
no_requests = math.floor(no_rows / 100)

# dataframe
res_pd = pd.DataFrame()

for i in tqdm(range(no_requests)):
    start_val = i*100
    results = edan.metadata_search(edan_schema="transproject", AppID=settings.AppID, AppKey=settings.AppKey, rows=100, start=start_val)
    res_pd = pd.concat([res_pd, pd.json_normalize(results['rows'])])


current_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
res_pd.to_excel("TC_projects_{}.xlsx".format(current_time), index=False)
