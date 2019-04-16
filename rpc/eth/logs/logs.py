# eth_blockNumber
# eth_getBlockByHash
# eth_getBlockByNumber

from utils.Utils import Mockable
from core.rpc_direct_core import RPCDirectCore
from utils.Utils import Config


from rpc.eth.enums.enums_eth_call import EnumsEthCall

from rpc.eth.enums.enums_execution_type import EnumsExecutionType
from rpc.eth.enums.enums_block_status import EnumsBlockStatus
from dto.log_filter_dto import LogFilterDTO

class Logs(object):

    def __init__(self, execution_type: EnumsExecutionType):
        self.execution_type = execution_type

    @Mockable("logs.filter_changes")
    def filter_changes(self, filter_id):
        return LogsService().call_filter_change_by_filter_id(filter_id)

    @Mockable("logs.filter_changes")
    def filter_id(self, filter_id):
        return LogsService().call_filter_logs_by_filter_id(filter_id)

    @Mockable("logs.filter_changes")
    def filter(self, filter:LogFilterDTO):
        return LogsService().call_filter_logs_by_filter(filter)


class LogsService:


    def call_filter_change_by_filter_id(self, filter_id):
        params = []
        params.append(filter_id)

        if Config.execution_type==EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_LOGS_FILTER_CHANGES, params=params)

    def call_filter_logs_by_filter_id(self, filter_id):
        params = []
        params.append(filter_id)

        if Config.execution_type==EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_LOGS_FILTER, params=params)

    def call_filter_logs_by_filter(self, filter):
        params = []
        params.append(filter.to_json(True))

        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_LO, params=params)
