# eth_blockNumber
# eth_getBlockByHash
# eth_getBlockByNumber

from src.utils.Utils import Mockable
from src.core.rpc_direct_core import RPCDirectCore
from src.utils.Utils import Config


from src.enums.enums_eth_call import EnumsEthCall

from src.enums.enums_execution_type import EnumsExecutionType

from src.core.in3_core import In3Core


class Account(object):

    def __init__(self, in3_core: In3Core):
        self.in3_core = in3_core

    @Mockable("account.all")
    def all(self):
        pass



# class AccountService:
#
#
#     def call_all_accounts(self):
#         if Config.execution_type==EnumsExecutionType.RPC_DIRECT:
#             return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_ACCOUNT_ALL)
