# This the automation file for voting process
import sys
import requests as req
import time
import random
from hashlib import sha256 
import pandas as pd
from datetime import datetime


def check_freedelivery(o_custkey, o_totalprice, o_orderdate):
    threshold = 200000
    total_spent = calc_totalspent(o_custkey, o_totalprice, o_orderdate)
    return (total_spent + float(o_totalprice) >= threshold)
        

def calc_totalspent(o_custkey, o_totalprice, o_orderdate):
    blockchain = req.get("http://127.0.0.1:8000/chain").json()["chain"]
    total_spent, flag = 0.0, 0
    
    for block_no in range(len(blockchain)-1,0,-1):
        print("inside block", block_no)
        for tx_no in range(len(blockchain[block_no]["transactions"])-1, -1, -1):
            print("inside tx", tx_no)
            
            tx_date = blockchain[block_no]["transactions"][tx_no]["o_orderdate"]
            spent_time = abs(int(o_orderdate[:4]) - int(tx_date[:4]))*365 + abs(int(o_orderdate[5:7]) - int(tx_date[5:7]))*30 + abs(int(o_orderdate[8:]) - int(tx_date[8:]))
            print(spent_time)
            tx_price = float(blockchain[block_no]["transactions"][tx_no]["o_totalprice"])
            tx_custkey = blockchain[block_no]["transactions"][tx_no]["o_custkey"]
            tx_freedelivery = bool(blockchain[block_no]["transactions"][tx_no]["o_freedelivery"])
            
            if spent_time <= 365:
                if o_custkey == tx_custkey:
                    if tx_freedelivery == False:
                        total_spent += tx_price
                    else:
                        return total_spent
            else:
                print(total_spent)
                return total_spent
    print(total_spent)
    return total_spent



url = "http://127.0.0.1:8000/new_transaction"

df = pd.read_csv("/home/ethereum/Downloads/ResearchData/data/order10k.csv")

for index in range(df.shape[0]):
    post_object = {
    "o_orderkey": str(df.iloc[index, 0]),
    "o_custkey": str(df.iloc[index, 1]),
    "o_totalprice": str(df.iloc[index, 2]),
    "o_orderdate": str(df.iloc[index, 3])
    }
    #post_object["o_freedelivery"] = str(check_freedelivery(post_object["o_custkey"], post_object["o_totalprice"], post_object["o_orderdate"]))

    req.post(url, json=post_object, headers={'Content-type':'application/json'})
    print("Order", index+1, "ingested successfully!")

#Threshold - 200000
print("Data Ingestion completed successfully...")