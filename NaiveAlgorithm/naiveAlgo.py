import json
import pandas as pd
import time

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("/home/ethereum/Downloads/ResearchData/data/order500k.csv")

# Record the start time for performance measurement
start_time = time.perf_counter()

# Set the threshold for free delivery
threshold = 200000

# Initialize a list to store free delivery status for each order
free_delivery = []

# Loop through each row in the DataFrame to check if free delivery is applicable
for i in range(df.shape[0]):
    if df.iloc[i, 2] >= threshold:
        free_delivery.append("yes")
    else:
        free_delivery.append("no")

# Add a new column for free delivery status to the DataFrame
df["free_delivery"] = free_delivery

# Save the DataFrame to a CSV file
df.to_csv("naiveReward500k.csv")

# Record the end time and calculate the processing time
end_time = time.perf_counter()
processing_time = end_time - start_time

# Load existing log data from a JSON file
with open("log.json") as file:
    data = json.load(file)

# Add the processing time for the naive approach to the log data
data["100K - naive"] = processing_time

# Corrected a typo in the mode used to open the file (changed 'w' to 'w+')
# Save the updated log data to the JSON file
with open("log.json", 'w') as file:
    json.dump(data, file)
