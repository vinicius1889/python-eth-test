from src.utils.Utils import Mockable
from src.core.rpc_direct_core import RPCDirectCore
from src.utils.Utils import Config


from src.enums.enums_eth_call import EnumsEthCall

from src.enums.enums_execution_type import EnumsExecutionType
from src.enums.enums_block_status import EnumsBlockStatus

from src.core.in3_core import In3Core


class Uncle(object):

    def __init__(self, in3_core:In3Core):
        self.in3_core = in3_core

    def count_by_blockhash(self, hash):
        params = []
        params.append(hash)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_UNCLE_COUNT_BY_BLOCK_HASH, params)


    def count_by_blocknumber(self, number):
        params = []
        params.append(number)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_UNCLE_COUNT_BY_BLOCK_NUMBER, params)


    def by_blockhash_and_index(self, hash, index):
        params = []
        params.append(hash)
        params.append(index)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_UNCLE_BY_BLOCKHASH_AND_INDEX, params)


    def by_blocknumber_and_index(self, number, index):
        params = []
        params.append(number)
        params.append(index)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_UNCLE_BY_BLOCKNUMBER_AND_INDEX, params)

