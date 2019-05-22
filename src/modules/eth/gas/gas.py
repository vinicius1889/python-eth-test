# eth_blockNumber
# eth_getBlockByHash
# eth_getBlockByNumber

from src.utils.Utils import Mockable
from src.core.rpc_direct_core import RPCDirectCore
from src.utils.Utils import Config


from src.enums.enums_eth_call import EnumsEthCall

from src.enums.enums_execution_type import EnumsExecutionType
from src.core.in3_core import In3Core


class Gas(object):

    def __init__(self, in3_core: In3Core):
        self.in3_core = in3_core

    def price(self):
        return self.in3_core.in3_eth_get_gas_price()


