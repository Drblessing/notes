# Hardhat

## Installing

Install

```
npm install --save-dev hardhat
npx hardhat
Create a typescript project
npm install --save-dev @nomicfoundation/hardhat-toolbox
```

Hardhat-toolbox includes the recommended plugins:

```
// hardhat.config.js
require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.9",
};
```

## Install chainlink and openzeppelin contracts

```
npm i @chainlink/contracts
npm i @openzeppelin/contracts
```

## General

Hardhat is based on tasks and plugins, to get tasks, run:

```
npx hardhat
```

To compile:

```
npx hardhat compile
```

## Verifying In Deploy Script

https://hardhat.org/hardhat-runner/plugins/nomiclabs-hardhat-etherscan#complex-arguments

Config

```
import { HardhatUserConfig } from 'hardhat/config';
import '@nomicfoundation/hardhat-toolbox';
import 'dotenv/config';
import '@nomiclabs/hardhat-etherscan';

const PRIVATE_KEY: string = process.env.PRIVATE_KEY ?? 'default';
const POLYGON_SCAN: string = process.env.POLYGON_SCAN_API_KEY ?? 'default';
const config: HardhatUserConfig = {
  defaultNetwork: 'hardhat',
  networks: {
    hardhat: {},
    matic: {
      url: 'https://rpc-mumbai.maticvigil.com',
      accounts: [PRIVATE_KEY],
    },
    fork_mumbai: {
      url: 'https://polygon-mumbai.g.alchemy.com/v2/BNUuST5J0QnWZ47NhzBJOzsFSnl7BXKN',
      accounts: [PRIVATE_KEY],
    },
  },
  etherscan: {
    apiKey: { polygonMumbai: POLYGON_SCAN },
  },
  solidity: '0.8.16',
};

export default config;
```

API key needs to go in etherscan.

Then, the deployment script:

```
import { ethers } from 'hardhat';
import hre from 'hardhat';

const main = async () => {
  const [owner, addr1, addr2] = await ethers.getSigners();
  const contractName = 'ProgramVRFConsumer';
  const contractFactory = await ethers.getContractFactory(contractName);

  const contractInstance = await contractFactory.deploy({});
  await contractInstance.deployTransaction.wait(5);
  console.log('Contract instance deployed to:', contractInstance.address);

  await hre.run('verify:verify', {
    network: 'matic',
    address: contractInstance.address,
  });
};
```

We use `hre.run('verify'...)` after 5 confirmations with `.wait(5)`

Arguments to verify

    network: 'matic',
    contract: 'contracts/utils/PolygonVRFConfig.sol:PolygonVRFConfig',
    address: contractInstance.address,

Constructor Variables:

```
import { constructorArguments } from './arguments';
export const constructorArguments = [1327];
  await hre.run('verify:verify', {
    network: 'matic',
    contract: 'contracts/utils/SuperConsumer.sol',
    address: contractInstance.address,
    constructorArguments,
  });
```

Need to specify which contract when we use Inheritance because it doesn't know which contract was deployed

## Forking EVM net

To fork an evm net, we need to use an acrhive node like Alchemy to fork the state of the current main net and then test functions

## Debugging

Try `npx hardhat clean` to fix JSON errors with artifacts and stuff

## Complex Deploy and contract interaction strips

```
const getTheAbi = (name: string) => {
  try {
    const dir = path.resolve(
      __dirname,
      `./artifacts/contracts/${name}.sol/${name}.json`
    );
    const file = fs.readFileSync(dir.replace('/scripts', ''), 'utf8');
    const json = JSON.parse(file);
    const abi = json.abi;
    return abi;
  } catch (e) {
    console.log(`e`, e);
  }
};

const send_transactions = async (consumerAddress: any) => {
  const [owner] = await ethers.getSigners();
  const abi = getTheAbi('PolygonVRF');
  const vrf = new ethers.Contract(consumerAddress, abi, owner);
  await vrf.requestRandomWords();
};

const addConsumer = async (address: any) => {
  const [owner] = await ethers.getSigners();
  const abi = getTheAbi('VRFSubscriber');
  const vrf = new ethers.Contract(
    '0xda3560218d7f9fd9cfe35568011d4518f8f4c26c',
    abi,
    owner
  );
  await vrf.addConsumer(address);
};

const workflow = async () => {
  const subAddress = await main();

  console.log(subAddress, typeof subAddress);
  // await addConsumer(subAddress);
  // await send_transactions('0x01b411be1B366669207717960684ac1789e41964');
};

workflow().catch((error) => {
  console.error(error);
  console.log('ERROR DEPLOY');
  process.exitCode = 1;
});
```

## Testing

Testing happens with ethers.js and Mocha.
We create a directory called `test`, and write some example test using `Chai`, a JavaScript assertion library:

```
const { expect } = require("chai");

describe("Token contract", function () {
  it("Deployment should assign the total supply of tokens to the owner", async function () {
    const [owner] = await ethers.getSigners();

    const Token = await ethers.getContractFactory("Token");

    const hardhatToken = await Token.deploy();

    const ownerBalance = await hardhatToken.balanceOf(owner.address);
    expect(await hardhatToken.totalSupply()).to.equal(ownerBalance);
  });
});
```

To send transactions and use multiple accounts:

```
// ...previous tests ...
  it("Should transfer tokens between accounts", async function() {
    const [owner, addr1, addr2] = await ethers.getSigners();

    const Token = await ethers.getContractFactory("Token");

    const hardhatToken = await Token.deploy();

    // Transfer 50 tokens from owner to addr1
    await hardhatToken.transfer(addr1.address, 50);
    expect(await hardhatToken.balanceOf(addr1.address)).to.equal(50);

    // Transfer 50 tokens from addr1 to addr2
    await hardhatToken.connect(addr1).transfer(addr2.address, 50);
    expect(await hardhatToken.balanceOf(addr2.address)).to.equal(50);
  });
});
```

`Fixtures` can help use reuse code and network state, making tests faster and code more DRY

```
const { loadFixture } = require("@nomicfoundation/hardhat-network-helpers");
const { expect } = require("chai");

describe("Token contract", function () {
  async function deployTokenFixture() {
    const Token = await ethers.getContractFactory("Token");
    const [owner, addr1, addr2] = await ethers.getSigners();

    const hardhatToken = await Token.deploy();

    await hardhatToken.deployed();

    // Fixtures can return anything you consider useful for your tests
    return { Token, hardhatToken, owner, addr1, addr2 };
  }

  it("Should assign the total supply of tokens to the owner", async function () {
    const { hardhatToken, owner } = await loadFixture(deployTokenFixture);

    const ownerBalance = await hardhatToken.balanceOf(owner.address);
    expect(await hardhatToken.totalSupply()).to.equal(ownerBalance);
  });

  it("Should transfer tokens between accounts", async function () {
    const { hardhatToken, owner, addr1, addr2 } = await loadFixture(
      deployTokenFixture
    );

    // Transfer 50 tokens from owner to addr1
    await expect(
      hardhatToken.transfer(addr1.address, 50)
    ).to.changeTokenBalances(hardhatToken, [owner, addr1], [-50, 50]);

    // Transfer 50 tokens from addr1 to addr2
    // We use .connect(signer) to send a transaction from another account
    await expect(
      hardhatToken.connect(addr1).transfer(addr2.address, 50)
    ).to.changeTokenBalances(hardhatToken, [addr1, addr2], [-50, 50]);
  });
});
```

Full test suite:

```
// This is an example test file. Hardhat will run every *.js file in `test/`,
// so feel free to add new ones.

// Hardhat tests are normally written with Mocha and Chai.

// We import Chai to use its asserting functions here.
const { expect } = require("chai");

// We use `loadFixture` to share common setups (or fixtures) between tests.
// Using this simplifies your tests and makes them run faster, by taking
// advantage of Hardhat Network's snapshot functionality.
const { loadFixture } = require("@nomicfoundation/hardhat-network-helpers");

// `describe` is a Mocha function that allows you to organize your tests.
// Having your tests organized makes debugging them easier. All Mocha
// functions are available in the global scope.
//
// `describe` receives the name of a section of your test suite, and a
// callback. The callback must define the tests of that section. This callback
// can't be an async function.
describe("Token contract", function () {
  // We define a fixture to reuse the same setup in every test. We use
  // loadFixture to run this setup once, snapshot that state, and reset Hardhat
  // Network to that snapshopt in every test.
  async function deployTokenFixture() {
    // Get the ContractFactory and Signers here.
    const Token = await ethers.getContractFactory("Token");
    const [owner, addr1, addr2] = await ethers.getSigners();

    // To deploy our contract, we just have to call Token.deploy() and await
    // its deployed() method, which happens onces its transaction has been
    // mined.
    const hardhatToken = await Token.deploy();

    await hardhatToken.deployed();

    // Fixtures can return anything you consider useful for your tests
    return { Token, hardhatToken, owner, addr1, addr2 };
  }

  // You can nest describe calls to create subsections.
  describe("Deployment", function () {
    // `it` is another Mocha function. This is the one you use to define each
    // of your tests. It receives the test name, and a callback function.
    //
    // If the callback function is async, Mocha will `await` it.
    it("Should set the right owner", async function () {
      // We use loadFixture to setup our environment, and then assert that
      // things went well
      const { hardhatToken, owner } = await loadFixture(deployTokenFixture);

      // `expect` receives a value and wraps it in an assertion object. These
      // objects have a lot of utility methods to assert values.

      // This test expects the owner variable stored in the contract to be
      // equal to our Signer's owner.
      expect(await hardhatToken.owner()).to.equal(owner.address);
    });

    it("Should assign the total supply of tokens to the owner", async function () {
      const { hardhatToken, owner } = await loadFixture(deployTokenFixture);
      const ownerBalance = await hardhatToken.balanceOf(owner.address);
      expect(await hardhatToken.totalSupply()).to.equal(ownerBalance);
    });
  });

  describe("Transactions", function () {
    it("Should transfer tokens between accounts", async function () {
      const { hardhatToken, owner, addr1, addr2 } = await loadFixture(
        deployTokenFixture
      );
      // Transfer 50 tokens from owner to addr1
      await expect(
        hardhatToken.transfer(addr1.address, 50)
      ).to.changeTokenBalances(hardhatToken, [owner, addr1], [-50, 50]);

      // Transfer 50 tokens from addr1 to addr2
      // We use .connect(signer) to send a transaction from another account
      await expect(
        hardhatToken.connect(addr1).transfer(addr2.address, 50)
      ).to.changeTokenBalances(hardhatToken, [addr1, addr2], [-50, 50]);
    });

    it("should emit Transfer events", async function () {
      const { hardhatToken, owner, addr1, addr2 } = await loadFixture(
        deployTokenFixture
      );

      // Transfer 50 tokens from owner to addr1
      await expect(hardhatToken.transfer(addr1.address, 50))
        .to.emit(hardhatToken, "Transfer")
        .withArgs(owner.address, addr1.address, 50);

      // Transfer 50 tokens from addr1 to addr2
      // We use .connect(signer) to send a transaction from another account
      await expect(hardhatToken.connect(addr1).transfer(addr2.address, 50))
        .to.emit(hardhatToken, "Transfer")
        .withArgs(addr1.address, addr2.address, 50);
    });

    it("Should fail if sender doesn't have enough tokens", async function () {
      const { hardhatToken, owner, addr1 } = await loadFixture(
        deployTokenFixture
      );
      const initialOwnerBalance = await hardhatToken.balanceOf(owner.address);

      // Try to send 1 token from addr1 (0 tokens) to owner (1000 tokens).
      // `require` will evaluate false and revert the transaction.
      await expect(
        hardhatToken.connect(addr1).transfer(owner.address, 1)
      ).to.be.revertedWith("Not enough tokens");

      // Owner balance shouldn't have changed.
      expect(await hardhatToken.balanceOf(owner.address)).to.equal(
        initialOwnerBalance
      );
    });
  });
});
```

Output:

```
$ npx hardhat test

  Token contract
    Deployment
      ✓ Should set the right owner
      ✓ Should assign the total supply of tokens to the owner
    Transactions
      ✓ Should transfer tokens between accounts (199ms)
      ✓ Should fail if sender doesn’t have enough tokens
      ✓ Should update balances after transfers (111ms)


  5 passing (1s)
```

You can add console.log statements which will output to the console on nodes and during test:

```
function transfer(address to, uint256 amount) external {
    require(balances[msg.sender] >= amount, "Not enough tokens");

    console.log(
        "Transferring from %s to %s %s tokens",
        msg.sender,
        to,
        amount
    );

    balances[msg.sender] -= amount;
    balances[to] += amount;

    emit Transfer(msg.sender, to, amount);
}

$ npx hardhat test

  Token contract
    Deployment
      ✓ Should set the right owner
      ✓ Should assign the total supply of tokens to the owner
    Transactions
Transferring from 0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266 to 0x70997970c51812dc3a010c7d01b50e0d17dc79c8 50 tokens
Transferring from 0x70997970c51812dc3a010c7d01b50e0d17dc79c8 to 0x3c44cdddb6a900fa2b585dd299e03d12fa4293bc 50 tokens
      ✓ Should transfer tokens between accounts (373ms)
      ✓ Should fail if sender doesn’t have enough tokens
Transferring from 0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266 to 0x70997970c51812dc3a010c7d01b50e0d17dc79c8 50 tokens
Transferring from 0x70997970c51812dc3a010c7d01b50e0d17dc79c8 to 0x3c44cdddb6a900fa2b585dd299e03d12fa4293bc 50 tokens
      ✓ Should update balances after transfers (187ms)


  5 passing (2s)
```

Deployed to mainnet is not technically different then deploying to local hardhat network or test networks. We first add the networks we want to deploy to and our private key of the account deploying in our config file:

```
require("@nomicfoundation/hardhat-toolbox");

// Go to https://www.alchemyapi.io, sign up, create
// a new App in its dashboard, and replace "KEY" with its key
const ALCHEMY_API_KEY = "KEY";

// Replace this private key with your Goerli account private key
// To export your private key from Metamask, open Metamask and
// go to Account Details > Export Private Key
// Beware: NEVER put real Ether into testing accounts
const GOERLI_PRIVATE_KEY = "YOUR GOERLI PRIVATE KEY";

module.exports = {
  solidity: "0.8.9",
  networks: {
    goerli: {
      url: `https://eth-goerli.alchemyapi.io/v2/${ALCHEMY_API_KEY}`,
      accounts: [GOERLI_PRIVATE_KEY]
    }
  }
};
```

Then run:

```
npx hardhat run scripts/deploy.js --network goerli
```
