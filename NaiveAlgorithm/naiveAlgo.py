import json
import pandas as pd

df = pd.read_csv("/home/ethereum/Downloads/ResearchData/data/order500k.csv")

threshold = 200000

free_delivery = []
for i in range(df.shape[0]):
    if(df.iloc[i, 2] >= threshold)):
        free_delivery.append("yes")
    else:
        free_delivery.append("no")

df["free_delivery"] = free_delivery

df.to_csv("naiveReward500k.csv")