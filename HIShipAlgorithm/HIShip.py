import pandas as pd
import json
import time

df = pd.read_csv("/home/blockchain/Blockchain-Powered-Free-Delivery-System-master/Data/order100k.csv")

start_time = time.perf_counter()
column = []
for i in range(df.shape[0]):
    column.append("no")
print(column)

df["o_freedelivery"] = column
df.head()


def check_freedelivery(total_spent, o_totalprice):
    threshold = 200000
    if (total_spent + float(o_totalprice) >= threshold):
        return "yes"
    else:
        return "no"

def calc_total(o_custkey, o_orderdate, chain):
    total_spent = 0
    for i in range(chain.shape[0]-1,-1,-1):
        tx_date = chain.iloc[i, 3]
        spent_time = int(o_orderdate[:4]) - int(tx_date[:4]) + int(o_orderdate[5:7])/12 - int(tx_date[5:7])/12 + int(o_orderdate[8:])/365 - int(tx_date[8:])/365
        tx_price = round(chain.iloc[i, 2])
        tx_custkey = chain.iloc[i, 1]
        tx_freedelivery = chain.iloc[i, 4]
            
        if spent_time <= 1:
            if o_custkey == tx_custkey:
                if tx_freedelivery == "no":
                    total_spent += tx_price
                else:
                    return total_spent
        else:
            return total_spent
    return total_spent


for tx_no in range(df.shape[0]):
    total_spent = calc_total(df.iloc[tx_no, 1], df.iloc[tx_no, 3], df.iloc[:tx_no])
    print(tx_no,":",total_spent, end= "=>")
    print(check_freedelivery(total_spent, df.iloc[tx_no, 2]))
    df.iloc[tx_no, 4] = check_freedelivery(total_spent, df.iloc[tx_no, 2])


df.to_csv("chainReward1M.csv")

end_time = time.perf_counter()

processing_time = end_time - start_time
with open("log.json") as file:
    data = json.load(file)
    
data["100K - chain"] = processing_time

with open("log.json", w) as file:
    json.dump(data, file)
    
