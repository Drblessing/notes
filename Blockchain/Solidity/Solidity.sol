// Contracts with owners
// https://docs.openzeppelin.com/contracts/4.x/access-control
// contracts/MyContract.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";

// Ownable Source
// https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.7.3/contracts/access/Ownable.sol
// Context Source
// https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/Context.sol

contract MyContract is Ownable {
    function normalThing() public {
        // anyone can call this normalThing()
    }

    function specialThing() public onlyOwner {
        // only the owner can call specialThing()!
    }
}

// WARNING: TONS OF CARE IS NEEDED
// Destroyable
// https://github.com/ConsenSysMesh/openzeppelin-solidity/blob/master/contracts/lifecycle/Destructible.sol
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.16;
import "@openzeppelin/contracts/access/Ownable.sol";
contract Destructible is Ownable {
    address payable payableOwner = payable(owner());
    constructor() payable {
    }
    /**
     * @dev Transfers the current balance to the owner and terminates the contract.
     */
    function destroy() public onlyOwner {
        selfdestruct(payableOwner);
    }
    function destroyAndSend(address payable _recipient) public onlyOwner {
        selfdestruct(_recipient);
    }
}


// Make address payable
// https://ethereum.stackexchange.com/questions/65693/how-to-cast-address-to-address-payable-in-solidity-0-5-0
address addr = 0x****;
address payable wallet = payable(addr);

MyContract addr = MyContract(0x****);
address payable wallet = payable(address(addr));