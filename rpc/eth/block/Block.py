# eth_blockNumber
# eth_getBlockByHash
# eth_getBlockByNumber

from utils.Utils import Mockable
from core.rpc_direct_core import RPCDirectCore
from utils.Utils import Config


from rpc.eth.enums.enums_eth_call import EnumsEthCall

from rpc.eth.enums.enums_execution_type import EnumsExecutionType
from rpc.eth.enums.enums_block_status import EnumsBlockStatus


class Block(object):

    def __init__(self, execution_type: EnumsExecutionType):
        self.execution_type = execution_type

    @Mockable("block.number")
    def number(self):
        return BlockService().call_number()

    @Mockable("block.byHash")
    def by_hash(self, hash, full=False):
        return BlockService().call_by_hash(hash=hash, full=full)

    @Mockable("block.byNumber")
    def by_number(self, number, full=False):
        if isinstance(number,EnumsBlockStatus):
            number = number.value
        return BlockService().call_by_number(number=number,full=full)



class BlockService:

    def call_number(self):
        if Config.execution_type==EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_BLOCK_NUMBER)

    def call_by_hash(self, hash, full):
        params = []
        params.append(hash)
        params.append(full)

        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_BLOCK_BY_HASH, params=params)

    def call_by_number(self, number, full):
        params = []
        params.append(number)
        params.append(full)

        if Config.execution_type==EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_BLOCK_BY_NUMBER, params=params)
