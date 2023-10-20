
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import "@openzeppelin/contracts/utils/Strings.sol";
contract HIShip{

struct Order {
    string o_orderkey;
    string o_custkey;
    string o_itemkey;
    uint o_totalprice;
    bool o_freedelivery;
    uint timestamp;}

Order[] public Orders;

function Genesis() public returns(Order[] memory) {
Order  memory order;
order.o_orderkey = "0";
order.o_custkey = "C000";
order.o_itemkey = "I0000";
order.o_totalprice = 0;
order.timestamp = block.timestamp;
order.o_freedelivery = false;

Orders.push(order);
return Orders;

}

function Buy(string memory o_custkey, string memory o_itemkey, uint o_totalprice) public returns(Order[] memory){
Order  memory order;
order.o_orderkey = Strings.toString(Orders.length);
order.o_custkey = o_custkey;
order.o_itemkey = o_itemkey;
order.o_totalprice = o_totalprice;
order.timestamp = block.timestamp;
order.o_freedelivery = Check(order.o_custkey, order.o_totalprice, order.timestamp);

Orders.push(order);
return Orders;
}


function Check(string memory o_custkey, uint o_totalprice, uint timestamp) private view returns(bool){
  uint total = o_totalprice;
  for(uint i=Orders.length-1; i > 0; i--){
    if((timestamp - Orders[i].timestamp) <= 120){
      if(keccak256(bytes(o_custkey)) == keccak256(bytes(Orders[i].o_custkey))){
            if(Orders[i].o_freedelivery == false)
                total += Orders[i].o_totalprice;
            else
                return total >= 499;
      }
    }
    else 
        return total >= 499;
  }
  return total >= 499; 
}


}
