// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import "@openzeppelin/contracts/utils/Strings.sol";

contract HIShip {
    // Define a struct to represent an order
    struct Order {
        string o_orderkey;
        string o_custkey;
        string o_itemkey;
        uint o_totalprice;
        bool o_freedelivery;
        uint timestamp;
    }

    // Array to store all orders
    Order[] public Orders;

    // Genesis function to initialize the contract with a default order
    function Genesis() public returns (Order[] memory) {
        Order memory order;
        order.o_orderkey = "0";
        order.o_custkey = "C000";
        order.o_itemkey = "I0000";
        order.o_totalprice = 0;
        order.timestamp = block.timestamp;
        order.o_freedelivery = false;

        // Add the genesis order to the Orders array
        Orders.push(order);
        return Orders;
    }

    // Buy function to create a new order
    function Buy(string memory o_custkey, string memory o_itemkey, uint o_totalprice) public returns (Order[] memory) {
        Order memory order;
        order.o_orderkey = Strings.toString(Orders.length);
        order.o_custkey = o_custkey;
        order.o_itemkey = o_itemkey;
        order.o_totalprice = o_totalprice;
        order.timestamp = block.timestamp;
        order.o_freedelivery = Check(order.o_custkey, order.o_totalprice, order.timestamp);

        // Add the new order to the Orders array
        Orders.push(order);
        return Orders;
    }

    // Check function to determine if free delivery is applicable
    function Check(string memory o_custkey, uint o_totalprice, uint timestamp) private view returns (bool) {
        uint total = o_totalprice;

        // Iterate through the Orders array in reverse order
        for (uint i = Orders.length - 1; i > 0; i--) {
            // Check if the timestamp difference is less than or equal to 120 seconds
            if ((timestamp - Orders[i].timestamp) <= 120) {
                // Check if the customer keys match
                if (keccak256(bytes(o_custkey)) == keccak256(bytes(Orders[i].o_custkey))) {
                    // Check if the previous order did not have free delivery
                    if (Orders[i].o_freedelivery == false)
                        total += Orders[i].o_totalprice;
                    else
                        // Return true if the total price is greater than or equal to 499
                        return total >= 499;
                }
            } else
                // Return true if the total price is greater than or equal to 499
                return total >= 499;
        }

        // Return true if the total price is greater than or equal to 499
        return total >= 499;
    }
}
