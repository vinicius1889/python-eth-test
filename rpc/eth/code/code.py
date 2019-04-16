# eth_blockNumber
# eth_getBlockByHash
# eth_getBlockByNumber

from utils.Utils import Mockable
from core.rpc_direct_core import RPCDirectCore
from utils.Utils import Config


from rpc.eth.enums.enums_eth_call import EnumsEthCall

from rpc.eth.enums.enums_execution_type import EnumsExecutionType
from rpc.eth.enums.enums_block_status import EnumsBlockStatus


class Code(object):

    def __init__(self, execution_type: EnumsExecutionType):
        self.execution_type = execution_type

    @Mockable("code.byAddressAndBlockNumber")
    def byAddressAndBlockNumber(self, address, number):
        if isinstance(number, EnumsBlockStatus):
            number = number.value

        return CodeService().call_code_by_address(address, number)



class CodeService:


    def call_code_by_address(self, address, number):
        params = []
        params.append(address)
        params.append(number)

        if Config.execution_type==EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_CODE_BY_ADDRESS_AND_NUMBER, params=params)
