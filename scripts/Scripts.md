# 🥾 Scripts

Howdy Partner!
This here is where I keep all my precious tools, like that trusty old python logger setup of mine.

| **Script**    | **Description**                                                                        |
| ------------- | -------------------------------------------------------------------------------------- |
| python_logger | A python logger setup that I use in all my projects.                                   |
| ethlibrary    | A library for working with ethereum numbers.                                           |
| hardhat       | A script for setting up a hardhat project.                                             |
| media         | Scripts for converting media files.                                                    |
| env loader    | A script for loading environment variables from a .env file. with extra functionality. |

## Usage

To use these scripts as command line tools, you have to:

1. Add a shebang line to the top of the script with the path to the program interpreter. For example, `#!/usr/bin/env python3` for, you gessed it, Python3.

2. Make the script executable with `chmod +x <script>`.

You're all set! For convenience you can also:

3. Add the script to your path. The bin folder of this Github is added to my path, so I put them there.

4. Rename the script to remove the extension. For example, `mv <script>.py <script>`.

5. Run it anywhere with `<script>`.

## Python Logger

My default python logging setup. Logs to a local .log file and optionally to the console. Includes the formatted date, log level, file name and line number, and the message.

## Eth Library

Containes classes for working with ethereum numbers and transactions. Will auto-calculate and convert Ethereum numbers to and from wei, gwei, and ether. Will auto-convert ethereum numbers to USD with apis, as well as current gas prices. Can input a few numbers into transaction and will auto-calculate transaction cost in USD, burnt eth, etc.

```python
from ethlibrary import EthNumber, EthTransaction

transaction_data = {
    "txn_hash": "0x5b4351ee81250db9d7ea57a3802c93f2f48e94efec251533bd4096029b38bd26",
    "status": True,
    "block": 17466051,
    "value": EthNumber(0.015, unit="ether"),
    "gas_price": EthNumber(14.334324056, unit="gwei"),
    "gas_used": 36745,
    "gas_fees_base": EthNumber(14.234324056, unit="gwei"),
    "gas_fees_max": EthNumber(18.899793035, unit="gwei"),
}

t = EthTransaction.from_dict(transaction_data)

print(t.txn_fee, t.txn_fee.usdp)
# 526714.737437720 gwei $0.99
```

## Convert

Opus to mp3
