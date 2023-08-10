import { ethers } from 'hardhat';
import readline from 'readline';

export async function warnIfMainnet() {
  // If network is mainnet, require confirmation from user input
  const ethersNetwork = await ethers.provider.getNetwork();
  const networkName = ethersNetwork.name;

  const mainnetNames = [
    'mainnet',
    'homestead',
    'polygon',
    'ethereum',
    'avalanche',
    'fantom',
    'xdai',
    'bsc',
    'arbitrum',
    'optimism',
    'base',
    'okex',
    'bnb',
  ];

  if (mainnetNames.includes(networkName)) {
    console.log(`WARNING: You are deploying to ${networkName}`.);
    console.log(`This will use real funds on ${networkName}`.);
    console.log('Are you sure? (y/n)');
    const input = await getUserInput();
    if (input !== 'y') {
      console.log('Exiting');
      process.exit();
    }
  }
}

async function getUserInput(): Promise<string> {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  return new Promise((resolve) => {
    rl.question('', (input) => {
      rl.close();
      resolve(input.trim());
    });
  });
}
