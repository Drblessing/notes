import 'dotenv/config';
export function rpc_url(networkName: string): string {
  if (networkName) {
    const uri = process.env[networkName.toUpperCase() + '_RPC'];
    if (uri && uri !== '') {
      return uri;
    }
  }

  return process.env.MUMBAI_RPC as string;
}

export function getMnemonic(): string {
  const mnemonic = process.env.DEV_SEED_PHRASE;
  if (!mnemonic || mnemonic === '') {
    return 'test test test test test test test test test test test junk';
  }
  return mnemonic;
}

export function accounts(): { mnemonic: string } {
  return { mnemonic: getMnemonic() };
}
