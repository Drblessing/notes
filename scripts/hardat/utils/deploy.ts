import { ethers } from 'hardhat';
import { verifyContract } from './verifyRuntime';

export async function mainDeploy(
  contractName: string,
  args: any[],
  value: string
) {
  const contract = await ethers.deployContract(contractName, args, {
    value,
  });

  await contract.waitForDeployment();

  await verifyContract(contract, args);

  const address = await contract.getAddress();

  console.log(`Deployed ${contractName} to ${address} with args ${args}`);

  return contract;
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
// main().catch((error) => {
//   console.error(error);
//   process.exitCode = 1;
// });
