# This the automation file for voting process
import sys
import requests as req
import time
import random
from hashlib import sha256 
import pandas as pd

url = "http://127.0.0.1:8080/new_transaction"

df = pd.read_csv("orders.csv")

for index in range(df.shape[0]):
    post_object = {
    'o_orderkey': df.iloc[index][0],
    'o_custkey': df.iloc[index][1],
    'o_totalprice': df.iloc[index][2],
    'o_orderdate': df.iloc[index][3]
    }
    req.post(url, json=post_object, headers={'Content-type':'application/json'})
    time.sleep(0.1)

#Threshold - 130000
print("Data Ingestion completed successfully...")