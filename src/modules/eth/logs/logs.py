
from src.enums.enums_eth_call import EnumsEthCall
from src.dto.log_filter_dto import LogFilterDTO
from src.core.in3_core import In3Core

class Logs(object):

    def __init__(self, in3_core: In3Core):
        self.in3_core = in3_core

    def filter_changes(self, filter_id):
        params = []
        params.append(filter_id)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_LOGS_FILTER_CHANGES, params)

    def by_filter_id(self, filter_id):
        params = []
        params.append(filter_id)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_LOGS_FILTER_ID, params)

    def by_filter(self, filter:LogFilterDTO):
        params = []
        params.append(filter.to_json(True))
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_LOGS_FILTER, params)


