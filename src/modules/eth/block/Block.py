# eth_blockNumber
# eth_getBlockByHash
# eth_getBlockByNumber

# from src.utils.Utils import Mockable
# from src.core.rpc_direct_core import RPCDirectCore
# from src.utils.Utils import Config


from src.enums.enums_eth_call import EnumsEthCall
from src.enums.enums_execution_type import EnumsExecutionType
from src.enums.enums_block_status import EnumsBlockStatus
from src.core.in3_core import In3Core


class Block:

    def __init__(self, in3_core: In3Core):
        self.in3_core = in3_core

    def number(self):
        return self.in3_core.in3_eth_blockNumber()

    def by_hash(self, hash, full=False):
        return self.in3_core.in3_eth_get_block_by_hash(hash, full)

    def by_number(self, number, full=False):
        if isinstance(number, EnumsBlockStatus):
            number = number.value
        return self.in3_core.in3_eth_get_block_by_number(number, full)

