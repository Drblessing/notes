from typing import Union, Literal, Optional
from decimal import Decimal, getcontext
from typing import NamedTuple, Optional
from datetime import datetime
import requests

getcontext().prec = 36


class EthNumber:
    """
    Class to represent, convert, and do arithmetic on Ethereum numbers.
    """

    UNITS = {
        "wei": Decimal(1),
        "gwei": Decimal(10**9),
        "ether": Decimal(10**18),
    }

    @staticmethod
    def get_current_price():
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
        )
        response.raise_for_status()  # Raise an exception if the request failed
        data = response.json()
        return Decimal(str(data["ethereum"]["usd"]))

    @staticmethod
    def get_current_gas_price():
        response = requests.get("https://ethgasstation.info/api/ethgasAPI.json?")
        response.raise_for_status()
        data = response.json()
        return data

    @property
    def usd(self) -> Decimal:
        eth_usd_price = self.get_current_price()
        return self._value / self.UNITS["ether"] * eth_usd_price

    @property
    def usdp(self) -> str:
        return f"${self.usd:.2f}"

    Unit = Union[Literal["wei"], Literal["gwei"], Literal["ether"]]

    def __init__(
        self,
        value: float | str | Decimal = 0,
        unit: Unit = "wei",
        tag: Optional[str] = None,
    ):
        self._value: Decimal = Decimal(str(value)) * self.UNITS[unit]
        self.tag = tag

    def __repr__(self):
        prefix = f"{self.tag}: " if self.tag else ""
        repr_value = self.repr_value(self._value)

        return f"{prefix}{repr_value}"

    @property
    def eth(self) -> Decimal:
        return self._value / self.UNITS["ether"]

    @property
    def ethp(self) -> str:
        return f"{self.eth:.18f}"

    @property
    def gwei(self) -> Decimal:
        return self._value / self.UNITS["gwei"]

    @property
    def gweip(self) -> str:
        return f"{self.gwei:.18f}"

    @staticmethod
    def repr_value(value: Decimal) -> str:
        if value >= 10**18:
            return f"{value / 10**18 } ether"
        elif value >= 10**9:
            return f"{value / 10**9 } gwei"
        else:
            return f"{value} wei"

    @property
    def value(self) -> Decimal:
        return self._value

    @value.setter
    def value(self, value: float | str | Decimal, unit: Unit = "wei"):
        self._value = Decimal(str(value)) * self.UNITS[unit]

    def __mul__(self, other: Union["EthNumber", int, float, str]) -> "EthNumber":
        if not isinstance(other, EthNumber):
            other = EthNumber(str(other))

        x = self.value * other.value
        return EthNumber(x)

    def __rmul__(self, other: Union["EthNumber", int, float, str]) -> "EthNumber":
        return self.__mul__(other)

    def __truediv__(self, other: Union["EthNumber", int, float, str]) -> "EthNumber":
        if not isinstance(other, EthNumber):
            other = EthNumber(str(other))

        x = self.value / other.value
        return EthNumber(x)

    def __rtruediv__(self, other: Union["EthNumber", int, float, str]) -> "EthNumber":
        if not isinstance(other, EthNumber):
            other = EthNumber(str(other))

        x = other.value / self.value
        return EthNumber(x)

    def __add__(self, other: Union["EthNumber", int, float, str]) -> "EthNumber":
        if not isinstance(other, EthNumber):
            other = EthNumber(str(other))

        x = self.value + other.value
        return EthNumber(x)

    def __radd__(self, other: Union["EthNumber", int, float, str]) -> "EthNumber":
        return self.__add__(other)

    def __sub__(self, other: Union["EthNumber", int, float, str]) -> "EthNumber":
        if not isinstance(other, EthNumber):
            other = EthNumber(str(other))

        x = self.value - other.value
        return EthNumber(x)

    def __rsub__(self, other: Union["EthNumber", int, float, str]) -> "EthNumber":
        if not isinstance(other, EthNumber):
            other = EthNumber(str(other))

        x = other.value - self.value
        return EthNumber(x)


class TransactionData(NamedTuple):
    txn_hash: str = "0x"
    status: Optional[bool] = None
    block: Optional[int] = None
    timestamp: Optional[datetime] = None
    from_address: Optional[str] = None
    to_address: Optional[str] = None
    value: Optional[EthNumber] = None
    gas_price: Optional[EthNumber] = None
    gas_limit: Optional[int] = None
    gas_used: Optional[int] = None
    gas_fees_base: Optional[EthNumber] = None
    gas_fees_max: Optional[EthNumber] = None
    gas_fees_max_priority: Optional[EthNumber] = None
    txn_savings: Optional[EthNumber] = None
    txn_type: Optional[str] = None


class EthTransaction:
    def __init__(self, data: TransactionData):
        self.txn_hash = data.txn_hash
        self.status = data.status
        self.block = data.block
        self.timestamp = data.timestamp
        self.from_address = data.from_address
        self.to_address = data.to_address
        self.value = data.value
        self.gas_price = data.gas_price or EthNumber(1, unit="gwei")
        self.gas_limit = data.gas_limit
        self.gas_used = data.gas_used or 21_000
        self.gas_fees_base = data.gas_fees_base or EthNumber(1, unit="gwei")
        self.gas_fees_max = data.gas_fees_max or EthNumber(1, unit="gwei")
        self.gas_fees_max_priority = data.gas_fees_max_priority
        self.txn_savings = data.txn_savings
        self.txn_type = data.txn_type

    @property
    def url(self) -> str:
        return f"https://etherscan.io/tx/{self.txn_hash}"

    @property
    def txn_fee(self) -> EthNumber:
        return self.gas_price * self.gas_used

    @property
    def burnt(self) -> EthNumber:
        return self.gas_fees_base * self.gas_used

    @property
    def savings(self) -> EthNumber:
        return self.gas_fees_max * self.gas_used - self.txn_fee

    @staticmethod
    def from_dict(data: dict) -> "EthTransaction":
        transaction_data = TransactionData(**data)
        return EthTransaction(transaction_data)
