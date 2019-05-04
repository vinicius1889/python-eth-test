# eth_blockNumber
# eth_getBlockByHash
# eth_getBlockByNumber

from src.utils.Utils import Mockable
from src.core.rpc_direct_core import RPCDirectCore
from src.utils.Utils import Config


from src.enums.enums_eth_call import EnumsEthCall

from src.enums.enums_execution_type import EnumsExecutionType


class Gas(object):

    def __init__(self, execution_type: EnumsExecutionType):
        self.execution_type = execution_type

    @Mockable("gas.price")
    def price(self):
        return GasService().call_gas_price()



class GasService:

    def call_gas_price(self):
        if Config.execution_type==EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_GAS_PRICE)
