# This is the automation file for the insgestion process
import sys
import requests as req
import time
import random
from hashlib import sha256 
import pandas as pd
from datetime import datetime


# Function to check if free delivery is applicable based on total spent
def check_freedelivery(o_custkey, o_totalprice, o_orderdate):
    threshold = 200000
    total_spent = calc_totalspent(o_custkey, o_totalprice, o_orderdate)
    return (total_spent + float(o_totalprice) >= threshold)


# Function to calculate total spent by a customer before a specific order date
def calc_totalspent(o_custkey, o_totalprice, o_orderdate):
    blockchain = req.get("http://127.0.0.1:8000/chain").json()["chain"]
    total_spent, flag = 0.0, 0
    
    for block_no in range(len(blockchain)-1, 0, -1):
        for tx_no in range(len(blockchain[block_no]["transactions"])-1, -1, -1):            
            tx_date = blockchain[block_no]["transactions"][tx_no]["o_orderdate"]
            spent_time = int(o_orderdate[:4]) - int(tx_date[:4]) + int(o_orderdate[5:7])/12 - int(tx_date[5:7])/12 + int(o_orderdate[8:])/365 - int(tx_date[8:])/365
            
            tx_price = float(blockchain[block_no]["transactions"][tx_no]["o_totalprice"])
            tx_custkey = blockchain[block_no]["transactions"][tx_no]["o_custkey"]
            tx_freedelivery = bool(blockchain[block_no]["transactions"][tx_no]["o_freedelivery"])
            
            # Check if the transaction is within 1 year and matches the customer and does not have free delivery
            if spent_time <= 1:
                if o_custkey == tx_custkey:
                    if tx_freedelivery == False:
                        total_spent += tx_price
                    else:
                        return total_spent
            else:
                return total_spent
    return total_spent


# URL for the new transaction endpoint
url = "http://127.0.0.1:8000/new_transaction"

# Read data from a CSV file into a Pandas DataFrame
df = pd.read_csv("/home/ethereum/Downloads/ResearchData/data/order10k.csv")

# Iterate through each row in the DataFrame to post transactions
for index in range(df.shape[0]):
    post_object = {
        "o_orderkey": str(df.iloc[index, 0]),
        "o_custkey": str(df.iloc[index, 1]),
        "o_totalprice": str(df.iloc[index, 2]),
        "o_orderdate": str(df.iloc[index, 3])
    }
    post_object["o_freedelivery"] = str(check_freedelivery(post_object["o_custkey"], post_object["o_totalprice"], post_object["o_orderdate"]))

    # Post the transaction to the specified URL
    req.post(url, json=post_object, headers={'Content-type':'application/json'})
    print("Order", index+1, "ingested successfully!")

# Threshold for free delivery - 200000
print("Data Ingestion completed successfully...")
