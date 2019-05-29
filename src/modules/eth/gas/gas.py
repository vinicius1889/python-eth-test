# eth_gasPrice

from src.enums.enums_eth_call import EnumsEthCall
from src.core.in3_core import In3Core


class Gas(object):

    def __init__(self, in3_core: In3Core):
        self.in3_core = in3_core

    def price(self):
        return self.in3_core.in3_raw_rpc(EnumsEthCall.RPC_GAS_PRICE.value, "[]")


