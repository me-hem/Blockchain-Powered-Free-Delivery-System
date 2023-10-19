
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HIShip{

uint length;
struct Order {
    string o_orderkey;
    string o_custkey;
    string o_itemkey;
    uint o_totalprice;
    bool o_freedelivery;
    uint timestamp;}

Order[] public Orders;

function Genesis() public view{
Order  memory order;
order.o_orderkey = "000";
order.o_custkey = "000";
order.o_itemkey = "000";
order.o_totalprice = 0;
order.timestamp = block.timestamp;
order.o_freedelivery = false;

Append(order);

}

function Buy(string memory o_custkey, string memory o_itemkey, uint o_totalprice) public view returns(Order memory){
Order  memory order;
order.o_orderkey = "0";
order.o_custkey = o_custkey;
order.o_itemkey = o_itemkey;
order.o_totalprice = o_totalprice;
order.o_freedelivery = Check(order.o_custkey, order.o_totalprice, order.timestamp);
order.timestamp = block.timestamp;
return(order);
}


function Check(string memory o_custkey, uint o_totalprice, uint timestamp) public pure returns(bool){

}



function Append(Order memory order) public {
Orders.push(order);
}
}




