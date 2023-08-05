import { ethers, run } from 'hardhat';

export async function verifyContract(deployedContract: any, args?: any[]) {
  // First check if the network is not hardhat or localhost
  const ethersNetwork = await ethers.provider.getNetwork();
  const networkName = ethersNetwork.name;

  if (networkName === 'hardhat' || networkName === 'localhost') {
    console.log(`Skipping contract verification on network: ${networkName}`);
    return;
  }

  const deployTxn = deployedContract.deploymentTransaction();
  const address = await deployedContract.getAddress();

  if (deployTxn == null || address == null) {
    throw new Error('Deployment transaction not found');
  }

  await deployTxn.wait(4);

  await run('verify:verify', {
    address: address,
    constructorArguments: args,
  });

  console.log(`Txn: ${deployTxn.hash}`);

  const tendrly = `https://dashboard.tenderly.co/tx/${networkName}/${deployTxn.hash}`;
  console.log(`Tenderly: ${tendrly}`);
}
