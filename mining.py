import sys
import requests as req
import time

port = sys.argv[1]
url = "http://127.0.0.1:8080/mine"

print("Mining started ")
count = 0
time.sleep(1)
while count < 3:
    time.sleep(20)
    res = req.get(url)
    print(res.content.decode('utf-8'))
    if res.content.decode('utf-8') == "No transactions to mine":
        count += 1

print("Mining completed successfully")
