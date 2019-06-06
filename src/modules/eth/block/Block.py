# eth_blockNumber
# eth_getBlockByHash
# eth_getBlockByNumber

import json
from src.enums.enums_eth_call import EnumsEthCall
from src.enums.enums_block_status import EnumsBlockStatus
from src.core.in3_core import In3Core


class Block:

    def __init__(self, in3_core: In3Core):
        self.in3_core = in3_core

    def number(self):
        return self.in3_core.in3_raw_rpc(EnumsEthCall.RPC_BLOCK_NUMBER.value, "[]")

    def by_hash(self, hash, full=False):
        params = []
        params.append(hash)
        params.append(full)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_BLOCK_BY_HASH, params)

    def by_number(self, number, full=False):
        params = []
        params.append(number)
        params.append(full)
        block = self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_BLOCK_BY_NUMBER, params)
        return json.loads(block)

