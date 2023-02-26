# **🔨 The best blockchain tools**

## **Development**

### - Hardhat

### - Remix

<br>

## **Debugging**

### - Remix debugger

### - Truffle debugger

### - Tenderly debugger

### - Etherscan

<br>

## **Testing**

### - Hardhat w/Chai & Mocha

### - Foundry w/fuzzing

<br>

## **Local Chain**

### - Hardhat w/Metamask

<br>

## **Testnets**

### - Mumbai

### - Sepolia

<br>

## **Node/RPC providers**

### - Infura

### - Alchemy

### - Chainlist.org

### - Running you own node 😄

<br>

## **Cold Wallets**

### - Ledger

### - Trezor

<br>

## **Mobile/Web Wallets**

### - Metamask

### - Trustwallet

<br>

## **Blockchains**

### - Ethereum

### - Polygon

### - Rollups

### - ZK Rollups

### - Bitcoin

<br> <br>

# **FAQs**

## **What is the best way to rapidly write and debug contracts?**

A mix of hardhat and remix!

<br>

## **How do I connect my metamask to Hardhat?**

1. Create local hardhat chain

```
npx hardhat node
```

2. Create hardhat network in metamask

```
Network Name: Hardhat
RPC Url: http://127.0.0.1:8545/
ChainID: 31337
Symbol: GO
```

3. Add local hardhat private key to metamask
   <br>The console should output private keys for the local chain, import these into metamask and rename account to "Hardhat."

4. Deploy any contracts that need to be on hardhat

```
npx hardhat run --network hardhat scripts/deploy.ts
```

5. Replace any constants in the app with the hardhat network address

<br>

## **How do I use openzeppelin and chainlink contracts in Hardhat?**

Since hardhat doesn't suport http imports, you'll need to use the npm package. Remix and truffle allow http imports in contracts, Hardhat does not for security reasons.

Install the packages:

```
npm i @chainlink/contracts
npm i @openzeppelin/contracts
```

Use them in solidity:

```
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";
```

<br>

## **What packages do I need for a hardhat project?**

Check out my sample Hardhat [package.json](https://github.com/Drblessing/utils/blob/master/Blockchain/Hardhat/package.json)
