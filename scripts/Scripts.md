# Scripts

Scripts I've written to make my life easier.

Scripts that are in my bin are moved to [here](/configs/bin).

To use these scripts, you have to:

1. Add a shebang line to the top of the script with the path to the program interpreter. For example, `#!/usr/bin/env python3` for Python 3.

2. Make the script executable with `chmod +x <script>`.

3. Add the script to your path. For example, `sudo cp <script> /usr/local/bin`. I have a directory ~/.local/bin in my path, so I put them there.

4. Rename the script to remove the extension. For example, `mv <script>.py <script>`.

5. Run it anywhere with `<script>`.

## Eth Library

Containes classes for working with ethereum numbers and transactions. Will auto-calculate and convert Ethereum numbers to and from wei, gwei, and ether. Will auto-convert ethereum numbers to USD with apis, as well as current gas prices. Can input a few numbers into transaction and will auto-calculate transaction cost in USD, burnt eth, etc.

Makes us of Python OOP features like dunder methods, properties, static methods, NamedTuples, and typehints.

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