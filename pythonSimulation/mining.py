import requests as req
import time

url = "http://127.0.0.1:8000/mine"

print("Mining started ")
count = 0
while count < 3:
    time.sleep(0.5)
    res = req.get(url)
    print(res.content.decode('utf-8'))
    if res.content.decode('utf-8') == "No transactions to mine":
        count += 1
    

blockchain = req.get("http://127.0.0.1:8000/chain").json()["chain"]
print("Mining completed successfully")
