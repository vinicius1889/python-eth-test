from src.utils.Utils import Mockable
from src.core.rpc_direct_core import RPCDirectCore
from src.utils.Utils import Config


from src.enums.enums_eth_call import EnumsEthCall

from src.enums.enums_execution_type import EnumsExecutionType


class Sign(object):

    def __init__(self, execution_type:EnumsEthCall):
        self.execution_type = execution_type

    @Mockable("sign.byAddress")
    def byAddress(self, address, data):
        return SignService().call_sign_by_address(address, data)


class SignService(object):

    def call_sign_by_address(self, address, data):
        params = []
        params.append(address)
        params.append(data)

        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_SIGN_BY_ADDRESS,
                                            params=params)






