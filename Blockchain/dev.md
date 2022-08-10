## **What are the best blockchain tools?**

### Testing

Hardhat

### Coding

Solidity

### Blockchains

Ethereum + Rollups

## **What is the best way to rapidly write and debug contracts?**

Hardhat

# Hardhat

## How do I connet metamask to Hardhat?

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
   <br>The console should output private keys for the local chain, import thest into metamask and rename account to "Hardhat"

4. Deploy any contracts that need to be on hardhat

```
npx hardhat run --network hardhat scripts/deploy.ts
```

5. Replace any constants in the app with the hardhat network address
