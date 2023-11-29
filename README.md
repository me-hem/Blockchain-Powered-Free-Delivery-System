# HIShip: Blockchain Powered Free Delivery System

## Outline
1. Abstract
2. HIShip Algorithm
3. Python based Blockchain Simulation
4. Solidity based Blockchain Simulation

   
### Abstract 
The emergence of online shopping was driven by the objective of delivering consumer products through a streamlined and user-friendly digital platform. Numerous challenges exist in the process of transitioning customers from conventional brick-and-mortar retail methods to the online shopping paradigm. Also retaining customers for online purchasing is a challenge, the customers have to pay some extra amount as the product handling fee and shipping charges for an order. Various online grocery retailers offer to minimize shipping fees through the implementation of distinct purchasing policies. Typically a customer gets the product delivery charge-free if they place an order of more than the threshold value. The customer who places an order frequently but with less amount than the threshold will have to pay the delivery charge every time no matter the cumulative sum of the order crosses the threshold. In this paper, we have a major focus on three points- 1. To make a fair ground for the sellers who intend to sell a product(s) that costs much less than a free shipping threshold. 2. To encourage those customers who prefer to buy more frequently with lesser order values. In opposite these existing policies, (i.e. free shipping on orders above Rs. 500/-) force customers to place an order that costs more than the free shipping threshold which is not customer-friendly. 3. To develop an algorithm that favors both seller and customer which can eventually increase the revenue of e-commerce websites like Flipkart, and Amazon.in, Myntra. To meet our objective, we have used the TPC-H standard data set. We use the blockchain paradigm to solve this problem in which the ordered transaction is stored in the blocks and a generated new block is appended to the blockchain. 

### HIShip Algorithm
1. Overview
  * The HIShip algorithm, implemented in Python using Pandas, introduces a data-driven approach to reward free delivery. Leveraging a CSV file (order10k.csv) as a data source, the algorithm initializes a DataFrame, incorporating a new "o_freedelivery" column.
  *  The core logic unfolds in two main functions: check_freedelivery assesses eligibility based on total spending, while calc_total calculates a customer's expenditure within a one-year timeframe before a specific order date.
  *  A systematic loop processes each transaction in the DataFrame, dynamically updating the "o_freedelivery" column. The results are then stored in a new CSV file (chainReward10K.csv). The algorithm's processing time is logged and appended to a JSON log file (log.json), providing insights into its performance across 10K to 500K transactions.

**2. Instructions to run alogorithm**
Clone the project,
```sh
$ git clone https://github.com/me-hem/Blockchain-Powered-Free-Delivery-System
```
Install the dependencies,
```sh
$ cd Blockchain-Powered-Free-Delivery-System/HIShipAlgorithm
$ pip install -r requirements.txt
```
Run the script
```sh
$ python3 HIShip.py
```


### Python based Blockchain Simulation
1. Blockchain Data Storage and computation
  * The simulation stores relevant data on the blockchain such as orderkey, custkey, totalprice, orderdate and freedelivery.
  * The simulation computes the freedelivery attribute for every transaction on-chain.

2. Consensus Algorithm:
  * Proof-of-Work (PoW) consensus mechanism implemented for block validation with difficulty 2.
  * PoW involves solving computationally intensive puzzles to add a block to the blockchain.

3. Data Persistence:
  * All relevant data is persistently stored on the blockchain.
  * Ensures transparency and integrity of the reward system.
  * The finalized blockchain is dumped to a JSON file for further analysis or sharing. JSON format chosen for its simplicity and compatibility.

4. Simulation Workflow:
  * Initialization: Create the initial blockchain structure.
  * Transaction Processing: Apply HIShip algorithm to determine free delivery eligibility.
  * PoW Consensus: Validate transactions through Proof-of-Work.
  * Blockchain Update: Add validated transactions to the blockchain.
  * JSON Dump: Save the final blockchain to a JSON file.

**5. Instructions to run application**

Clone the project,
```sh
$ git clone https://github.com/me-hem/Blockchain-Powered-Free-Delivery-System
```
Install the dependencies,
```sh
$ cd Blockchain-Powered-Free-Delivery-System/pythonSimulation
$ pip install -r requirements.txt
```
Start a blockchain node server,
```sh
# Windows users can follow this: https://flask.palletsprojects.com/en/1.1.x/cli/#application-discovery
$ export FLASK_APP=service.py
$ flask run --port 8000
```
One instance of our blockchain node is now up and running at port 8000.

Run the application on a different terminal session,
```sh
$ python3 app.py 5000
```
The application should be up and running at [http://localhost:5000](http://localhost:5000).

Now, run automation script simultaneously  i.e.

```sh
$ python3 ingest.py 8000& python3 mining.py 8000&
```
Now, you can see the chain at [http://localhost:8000/chain](http://localhost:8000/chain).

### Solidity based Blockchain Simulation
1. Contract Name: HIShip
  * Implementation of the HIShip algorithm on the Ethereum blockchain using the Solidity programming language.
  * An array is used to store all orders on the blockchain.

2. Buy Function
  * Creates a new order with the provided customer key, item key, and total price.
  * Determines free delivery eligibility using the Check function.
  * Adds the new order to the array of orders.
  * Returns the updated array of orders.

3. Check Function
  * Determines if free delivery is applicable based on the following conditions:
    + Checks the total price of the current order.
    + Compares the timestamp of the current order with previous orders.Considers a time window of 120 seconds for order history.
    + Evaluates the total price against a threshold of 499.
  * Returns a boolean indicating whether free delivery is applicable.

**4. Instructions to run simulation**

  * Clone the project,
```sh
$ git clone https://github.com/me-hem/Blockchain-Powered-Free-Delivery-System
```
  * Open remix
  * Upload HIShip.sol file from Blockchain-Powered-Free-Delivery-System/soliditySimulation
  * Deploy the contract
  * Execute genesis function to make genesis block
  * Execute buy function with required attribute.
  * See logs for transactions and output
   

