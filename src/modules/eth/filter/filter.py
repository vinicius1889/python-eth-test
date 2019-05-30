
from src.enums.enums_eth_call import EnumsEthCall
from src.dto.filter_dto import FilterDTO
from src.core.in3_core import In3Core

class Filter(object):

    def __init__(self, in3_core: In3Core):
        self.in3_core = in3_core

    def create(self, filter_dto:FilterDTO ):
        params = []
        params.append(filter_dto.to_json(True))
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_FILTER_NEW, params)

    def block_create(self):
        params = []
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_FILTER_NEW_BLOCK, params)

    def pending_transaction_create(self):
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_FILTER_NEW_PENDING_TRANSACTION, [])

    def uninstall(self, filter_id):
        params = []
        params.append(filter_id)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_FILTER_UNINSTALL, params)

