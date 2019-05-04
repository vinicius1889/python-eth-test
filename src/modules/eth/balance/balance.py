# eth_blockNumber
# eth_getBlockByHash
# eth_getBlockByNumber

from src.utils.Utils import Mockable
from src.core.rpc_direct_core import RPCDirectCore
from src.utils.Utils import Config


from src.enums.enums_eth_call import EnumsEthCall

from src.enums.enums_execution_type import EnumsExecutionType
from src.enums.enums_block_status import EnumsBlockStatus



class Balance(object):

    def __init__(self, execution_type: EnumsExecutionType):
        self.execution_type = execution_type

    @Mockable("balance")
    def of(self, address, number):
        if isinstance(number, EnumsBlockStatus):
            number = number.value

        return BalanceService().call_get_balance(address, number)



class BalanceService:


    def call_get_balance(self, address, number):
        params = []
        params.append(address)
        params.append(number)

        if Config.execution_type==EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_BALANCE_OF,params=params)
