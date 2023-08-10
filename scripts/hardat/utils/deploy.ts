import { ethers } from 'hardhat';
import { verifyContract } from './verifyRuntime';
import { warnIfMainnet } from './warnIfMainnet';

export async function mainDeploy(
  contractName: string,
  args: any[],
  value: string
) {
  await warnIfMainnet();

  const contract = await ethers.deployContract(contractName, args, {
    value,
  });

  await contract.waitForDeployment();

  await verifyContract(contract, args);

  const address = await contract.getAddress();

  console.log(`Deployed ${contractName} to ${address} with args ${args}`);

  return contract;
}
