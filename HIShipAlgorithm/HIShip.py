import pandas as pd
import json
import time

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("../TestData/order10k.csv")

# Initialize a new column with default value "no"
start_time = time.perf_counter()
column = []
for i in range(df.shape[0]):
    column.append("no")


df["o_freedelivery"] = column  # Add the new column to the DataFrame


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
    backtrack_count = 0
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
                    return total_spent, backtrack_count
        else:
            return total_spent, backtrack_count
        backtrack_count += 1
    return total_spent, backtrack_count

with open("backtrack_log10K.json") as back_file:
    backtrack_log = json.load(back_file)

# Loop through each row in the DataFrame to calculate total spent and check free delivery eligibility
for tx_no in range(df.shape[0]):
    total_spent, backtrack_count = calc_total(df.iloc[tx_no, 1], df.iloc[tx_no, 3], df.iloc[:tx_no])
    print(tx_no, ":", total_spent, end="=>")
    print(check_freedelivery(total_spent, df.iloc[tx_no, 2]))
    df.iloc[tx_no, 4] = check_freedelivery(total_spent, df.iloc[tx_no, 2])
    backtrack_log[str(df.iloc[tx_no, 1])] = str(backtrack_count)

# Save the DataFrame to a CSV file
df.to_csv("chainReward10K.csv")


with open("backtrack_log10K.json", 'w') as back_file:
    json.dump(backtrack_log, back_file)

end_time = time.perf_counter()
processing_time = end_time - start_time
with open("log.json") as file:
    data = json.load(file)

data["10K - HIShip"] = processing_time

# Save the updated log data to the JSON file
with open("log.json", 'w') as file:
    json.dump(data, file)

