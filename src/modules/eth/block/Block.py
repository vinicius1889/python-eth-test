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
        params = '["{0}", {1} ]'.format(hash,full.__str__().lower())
        return self.in3_core.in3_raw_rpc(EnumsEthCall.RPC_BLOCK_BY_HASH.value, params)

    def by_number(self, number, full=False):
        if isinstance(number, EnumsBlockStatus):
            number = number.value
        params = '["{0}",{1}]'.format(number,full.__str__().lower())
        block = self.in3_core.in3_raw_rpc(EnumsEthCall.RPC_BLOCK_BY_NUMBER.value, params)
        return json.loads(block)

