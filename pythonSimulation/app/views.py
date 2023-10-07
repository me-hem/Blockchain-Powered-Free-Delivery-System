import datetime
import json

import requests
from flask import render_template, redirect, request
from flask import flash
from app import app

import time

# The node with which our application interacts, there can be multiple
# such nodes as well.
CONNECTED_SERVICE_ADDRESS = "http://127.0.0.1:8000"

current_time = time.time()

def fetch_posts():
    pass

@app.route('/')
def index():
    fetch_posts()
    get_chain_address = "{}/chain".format(CONNECTED_SERVICE_ADDRESS)
    response = requests.get(get_chain_address)

    # retrieving chain length for calculating total number of blocks
    chain_length = response.json()["length"]
    
    # calculating time difference to calculate voting time
    if chain_length > 1:
        time_diff= datetime.datetime.fromtimestamp(response.json()["chain"][-1]["timestamp"]) - datetime.datetime.fromtimestamp(response.json()["chain"][1]["transactions"][0]["timestamp"])#datetime.datetime.fromtimestamp(current_time)
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        Voting_Time = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
            
    else:
        Voting_Time = "00:00:00"
    
    
    # calculating total mining time
    if chain_length > 1:
        temp_time = time_diff.seconds - (chain_length-1)*10
        mining_time = round(temp_time,4)
        # calculating average mining time
        average_time = round(temp_time/(chain_length-1),4)
    else:
        mining_time, average_time = 0, 0

    
    

    return render_template('index.html',
                           title='Blockchain-Powered Free Delivery System',
                           node_address=CONNECTED_SERVICE_ADDRESS,
                           readable_time=timestamp_to_string,
                           voting_time = Voting_Time,
                           length = chain_length-1,
                           average_time = average_time,
                           mining_time = mining_time)



def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M')
