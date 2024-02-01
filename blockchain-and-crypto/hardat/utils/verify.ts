import 'dotenv/config';

export function etherscan_api_key(networkName: string): string {
  if (networkName) {
    const uri = process.env[networkName.toUpperCase() + '_API_KEY'];
    if (uri && uri !== '') {
      return uri;
    }
  }

  return process.env.ETHERSCAN_API_KEY as string;
}
