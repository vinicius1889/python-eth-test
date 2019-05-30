from src.enums.enums_eth_call import EnumsEthCall
from src.core.in3_core import  In3Core


class Sign(object):

    def __init__(self, in3_core: In3Core):
        self.in3_core = in3_core

    def by_address(self, address, data):
        params = []
        params.append(address)
        params.append(data)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_SIGN_BY_ADDRESS, params)





