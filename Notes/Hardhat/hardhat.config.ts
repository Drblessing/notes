import { HardhatUserConfig } from 'hardhat/config';
import '@nomicfoundation/hardhat-toolbox';
import 'dotenv/config';
import '@nomiclabs/hardhat-etherscan';

const PRIVATE_KEY: string = process.env.PRIVATE_KEY ?? 'default';
const POLYGON_SCAN: string = process.env.POLYGON_SCAN_API_KEY ?? 'default';
const config: HardhatUserConfig = {
  defaultNetwork: 'matic',
  networks: {
    hardhat: {},
    matic: {
      url: 'https://rpc-mumbai.maticvigil.com',
      accounts: [PRIVATE_KEY],
    },
  },
  etherscan: {
    apiKey: POLYGON_SCAN,
  },
  solidity: '0.8.9',
};

export default config;
