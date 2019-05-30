

from src.enums.enums_eth_call import EnumsEthCall
from src.core.in3_core import In3Core


class Code(object):

    def __init__(self, in3_core: In3Core):
        self.in3_core = in3_core

    def by_address_and_number(self, address, number):
        params = []
        params.append(address)
        params.append(number)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_CODE_BY_ADDRESS_AND_NUMBER, params)
