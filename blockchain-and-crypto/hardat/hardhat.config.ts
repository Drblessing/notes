import { HardhatUserConfig } from 'hardhat/config';
import '@nomicfoundation/hardhat-toolbox';
import '@nomicfoundation/hardhat-foundry';
import { accounts, rpc_url } from './utils/network';
import { etherscan_api_key } from './utils/verify';
import 'hardhat-gas-reporter';

const config: HardhatUserConfig = {
  networks: {
    hardhat: {
      accounts: accounts(),
      forking: {
        url: rpc_url('polygon'),
        enabled: false,
      },
    },
    sepolia: {
      url: rpc_url('sepolia'),
      accounts: accounts(),
    },
    mumbai: {
      url: rpc_url('mumbai'),
      accounts: accounts(),
    },
    polygon: {
      url: rpc_url('polygon'),
      accounts: accounts(),
    },
  },
  solidity: {
    version: '0.8.19',
    settings: {
      optimizer: {
        enabled: true,
        runs: 200,
      },
    },
  },
  etherscan: {
    apiKey: {
      sepolia: etherscan_api_key('ETHERSCAN'),
      polygonMumbai: etherscan_api_key('POLYGONSCAN'),
      polygon: etherscan_api_key('POLYGONSCAN'),
    },
  },
};

export default config;
