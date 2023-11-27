import json
import pandas as pd
import time

df = pd.read_csv("/home/ethereum/Downloads/ResearchData/data/order500k.csv")

start_time = time.perf_counter()
threshold = 200000

free_delivery = []
for i in range(df.shape[0]):
    if(df.iloc[i, 2] >= threshold)):
        free_delivery.append("yes")
    else:
        free_delivery.append("no")

df["free_delivery"] = free_delivery

df.to_csv("naiveReward500k.csv")

end_time = time.perf_counter()

processing_time = end_time - start_time
with open("log.json") as file:
    data = json.load(file)
    
data["100K - naive"] = processing_time

with open("log.json", w) as file:
    json.dump(data, file)
