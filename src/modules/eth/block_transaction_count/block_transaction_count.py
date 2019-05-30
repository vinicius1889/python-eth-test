# eth_getBlockTransactionCountByNumber
# eth_getBlockTransactionCountByHash


from src.enums.enums_eth_call import EnumsEthCall
from src.core.in3_core import In3Core


class BlockTransactionCount:

    def __init__(self, in3_core:In3Core):
        self.in3_core = in3_core

    def byHash(self, hash):
        params = []
        params.append(hash)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_BLOCK_TRANSACTION_COUNT_BY_HASH, params)


    def byNumber(self, number):
        params = []
        params.append(number)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_BLOCK_TRANSACTION_COUNT_BY_NUMBER, params )


