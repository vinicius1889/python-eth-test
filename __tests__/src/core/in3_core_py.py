from unittest import TestCase
from src.core.in3_core import In3Core
from src.enums.enums_eth_call import EnumsEthCall
from src.enums.enums_block_status import EnumsBlockStatus

class In3CoreTest(TestCase):

    def testing_params(self):
        params = []
        params.append("0x123")
        params.append(True)
        params.append(EnumsBlockStatus.LATEST)

        In3Core().in3_raw_rpc_wrapper(EnumsEthCall.RPC_GAS_PRICE, params)
