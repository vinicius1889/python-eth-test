from src.utils.Utils import Mockable
from src.core.rpc_direct_core import RPCDirectCore
from src.utils.Utils import Config


from src.enums.enums_eth_call import EnumsEthCall

from src.enums.enums_execution_type import EnumsExecutionType
from src.enums.enums_block_status import EnumsBlockStatus



class BlockTransactionCount:

    def __init__(self, execution_type: EnumsExecutionType):
        self.execution_type = execution_type

    @Mockable("blockTransactionCount.byHash")
    def byHash(self, hash):
        return BlockTransactionCountService().call_by_hash(hash)

    @Mockable("blockTransactionCount.byNumber")
    def byNumber(self, number):
        if isinstance(number,EnumsBlockStatus):
            number = number.value
        return BlockTransactionCountService().call_by_number(number)



class BlockTransactionCountService:

    def __init__(self):
        pass

    def call_by_number(self,number):
        params = []
        params.append(number)

        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_BLOCK_TRANSACTION_COUNT_BY_NUMBER, params=params)

    def call_by_hash(self, hash):
        params = []
        params.append(hash)

        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_BLOCK_TRANSACTION_COUNT_BY_HASH, params=params)

