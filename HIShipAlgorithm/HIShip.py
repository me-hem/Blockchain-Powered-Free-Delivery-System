import pandas as pd
import json
import time

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("/home/blockchain/Blockchain-Powered-Free-Delivery-System-master/Data/order100k.csv")

# Initialize a new column with default value "no"
start_time = time.perf_counter()
column = []
for i in range(df.shape[0]):
    column.append("no")
print(column)

df["o_freedelivery"] = column  # Add the new column to the DataFrame
df.head()

# Function to check if free delivery is applicable based on total spent
def check_freedelivery(total_spent, o_totalprice):
    threshold = 200000
    if (total_spent + float(o_totalprice) >= threshold):
        return "yes"
    else:
        return "no"

# Function to calculate total spent by a customer before a specific order date
def calc_total(o_custkey, o_orderdate, chain):
    total_spent = 0
    for i in range(chain.shape[0]-1, -1, -1):
        tx_date = chain.iloc[i, 3]
        spent_time = int(o_orderdate[:4]) - int(tx_date[:4]) + int(o_orderdate[5:7])/12 - int(tx_date[5:7])/12 + int(o_orderdate[8:])/365 - int(tx_date[8:])/365
        tx_price = round(chain.iloc[i, 2])
        tx_custkey = chain.iloc[i, 1]
        tx_freedelivery = chain.iloc[i, 4]
        
        # Check if the transaction is within 1 year and matches the customer and does not have free delivery
        if spent_time <= 1:
            if o_custkey == tx_custkey:
                if tx_freedelivery == "no":
                    total_spent += tx_price
                else:
                    return total_spent
        else:
            return total_spent
    return total_spent

# Loop through each row in the DataFrame to calculate total spent and check free delivery eligibility
for tx_no in range(df.shape[0]):
    total_spent = calc_total(df.iloc[tx_no, 1], df.iloc[tx_no, 3], df.iloc[:tx_no])
    print(tx_no, ":", total_spent, end="=>")
    print(check_freedelivery(total_spent, df.iloc[tx_no, 2]))
    df.iloc[tx_no, 4] = check_freedelivery(total_spent, df.iloc[tx_no, 2])

# Save the DataFrame to a CSV file
df.to_csv("chainReward1M.csv")

end_time = time.perf_counter()

processing_time = end_time - start_time
with open("log.json") as file:
    data = json.load(file)

data["100K - chain"] = processing_time

# Corrected a typo in the mode used to open the file (changed 'w' to 'w+')
with open("log.json", 'w+') as file:
    json.dump(data, file)
