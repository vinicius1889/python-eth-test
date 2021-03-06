# eth_blockNumber
# eth_getBlockByHash
# eth_getBlockByNumber

from utils.Utils import Mockable
from core.rpc_direct_core import RPCDirectCore
from utils.Utils import Config


from rpc.eth.enums.enums_eth_call import EnumsEthCall

from rpc.eth.enums.enums_execution_type import EnumsExecutionType


class Account(object):

    def __init__(self, execution_type: EnumsExecutionType):
        self.execution_type = execution_type

    @Mockable("account.all")
    def all(self):
        return AccountService().call_all_accounts()



class AccountService:


    def call_all_accounts(self):
        if Config.execution_type==EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_ACCOUNT_ALL)
