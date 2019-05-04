from src.utils.Utils import Mockable
from src.core.rpc_direct_core import RPCDirectCore
from src.utils.Utils import Config


from src.enums.enums_eth_call import EnumsEthCall

from src.enums.enums_execution_type import EnumsExecutionType
from src.enums.enums_block_status import EnumsBlockStatus




class Uncle(object):

    def __init__(self, execution_type:EnumsEthCall):
        self.execution_type = execution_type

    @Mockable("uncle.countByBlockHash")
    def countByBlockHash(self, hash):
        return UncleService().call_uncle_count_by_block_hash(hash)


    @Mockable("uncle.countByBlockNumber")
    def countByBlockNumber(self, number):
        if isinstance(number, EnumsBlockStatus):
            number = number.value

        return UncleService().call_uncle_count_by_block_number(number=number)


    @Mockable("uncle.byBlockHashAndIndex")
    def byBlockHashAndIndex(self, hash, index):
        return UncleService().call_uncle_by_blockhash_and_index(hash, index)


    @Mockable("uncle.byBlockNumberAndIndex")
    def byBlockNumberAndIndex(self, number, index):
        if isinstance(number, EnumsBlockStatus):
            number = number.value

        return UncleService().call_uncle_by_blocknumber_and_index(number, index)


class UncleService(object):

    def call_uncle_count_by_block_hash(self, hash):
        params = []
        params.append(hash)
        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_UNCLE_COUNT_BY_BLOCK_HASH,
                                            params=params)


    def call_uncle_count_by_block_number(self, number):
        params = []
        params.append(number)
        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_UNCLE_COUNT_BY_BLOCK_NUMBER,
                                            params=params)


    def call_uncle_by_blockhash_and_index(self, hash, index):
        params = []
        params.append(hash)
        params.append(index)
        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_UNCLE_BY_BLOCKHASH_AND_INDEX,
                                            params=params)

    def call_uncle_by_blocknumber_and_index(self, number, index):
        params = []
        params.append(number)
        params.append(index)
        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_UNCLE_BY_BLOCKNUMBER_AND_INDEX,
                                            params=params)





