# eth_blockNumber
# eth_getBlockByHash
# eth_getBlockByNumber

from utils.Utils import Mockable
from core.rpc_direct_core import RPCDirectCore
from utils.Utils import Config
from rpc.eth.enums.enums_eth_call import EnumsEthCall
from rpc.eth.enums.enums_execution_type import EnumsExecutionType
from dto.filter_dto import FilterDTO


class Filter(object):

    def __init__(self, execution_type: EnumsExecutionType):
        self.execution_type = execution_type

    @Mockable("filter.create")
    def create(self, filter_dto:FilterDTO ):
        return FilterService().call_new_filter(filter_dto)

    @Mockable("filter.block")
    def block_create(self):
        return FilterService().call_block_create_filter()

    @Mockable("filter.pendingTransaction")
    def pending_transaction_create(self):
        return FilterService().call_pending_transaction_create()

    @Mockable("filter.uninstall")
    def uninstall(self, filter_id):
        return FilterService().call_uninstall(filter_id)


class FilterService:

    def call_new_filter(self, filter_dto:FilterDTO):
        params=[]
        params.append(filter_dto.to_json(True))

        if Config.execution_type==EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_FILTER_NEW, params=params )

    def call_block_create_filter(self):
        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_FILTER_NEW_BLOCK)

    def call_pending_transaction_create(self):
        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_FILTER_NEW_PENDING_TRANSACTION)

    def call_uninstall(self, id):
        params=[]
        params.append(id)
        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_FILTER_UNINSTALL, params=params)
