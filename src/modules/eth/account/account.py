# eth_accounts

import json

from src.enums.enums_eth_call import EnumsEthCall
from src.core.in3_core import In3Core


class Account(object):

    def __init__(self, in3_core: In3Core):
        self.in3_core = in3_core

    def all(self):
        params = '[]'
        accounts = self.in3_core.in3_raw_rpc(EnumsEthCall.RPC_ACCOUNT_ALL.value,params)
        return json.loads(accounts)
