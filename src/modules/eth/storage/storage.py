from src.enums.enums_eth_call import EnumsEthCall
from src.core.in3_core import In3Core


class Storage(object):

    def __init__(self, in3_core: In3Core):
        self.in3_core = in3_core

    def at(self, address, position, block_number):
        params = []
        params.append(address)
        params.append(position)
        params.append(block_number)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_STORAGE_AT, params)
