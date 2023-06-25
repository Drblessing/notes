## Inheriting Multiple Contracts

```
contract ProgramVRFConsumer is PolygonVRFConfig {
uint dummy = 7890;
}
contract Hackjack is VRFConsumerBaseV2, Destructible, BreakdownUint256 {


    constructor()
        payable
        VRFConsumerBaseV2(vrfCoordinator)
    {
```

## Constructor Inheritance

https://securitygrind.com/solidity-constructors-and-inheritance/

Indirect Constructor

```
contract fooOwned {
    uint256 val;
    constructor(uint256 _val) {
        val = _val;
    }
}

contract fooContract is fooOwned {
    constructor(uint256 _val) fooOwned (_val) {
        // Logic
    }
}
``` 

Explicit Constructor in contract init

```
contract fooOwned {
    uint256 val;
    constructor(uint256 _val) {
        val = _val;
    }
}

contract fooContract is fooOwned (7) {
    // Logic
}
```


## Delegate Call

https://stackoverflow.com/questions/50999801/call-external-solidity-contract-with-interface-and-delegatecall

For the record: When using delegatecall, you have to use the exact data type specification within the function string (uint256 instead of just uint). You also do not need to specify the parameter names. So a function with header function doSomething(uint \_num) public should be called like this delegatecall(bytes4(keccak256("doSomething(uint256)")),\_myVar).
