# eth_blockNumber
# eth_getBlockByHash
# eth_getBlockByNumber

from utils.Utils import Mockable
from core.rpc_direct_core import RPCDirectCore
from utils.Utils import Config


from rpc.eth.enums.enums_eth_call import EnumsEthCall

from rpc.eth.enums.enums_execution_type import EnumsExecutionType
from rpc.eth.enums.enums_block_status import EnumsBlockStatus


class Storage(object):

    def __init__(self, execution_type: EnumsExecutionType):
        self.execution_type = execution_type

    @Mockable("storage")
    def at(self, address, position, block_number):
        if isinstance(block_number, EnumsBlockStatus):
            number = block_number.value

        return StorageService().call_storage_at(address, position,number)



class StorageService:


    def call_storage_at(self, address, position, number):
        params = []
        params.append(address)
        params.append(position)
        params.append(number)

        if Config.execution_type==EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_STORAGE_AT, params=params)
