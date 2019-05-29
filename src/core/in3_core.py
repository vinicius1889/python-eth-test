from src.core.slib import libin3p as libin3
from src.enums.enums_eth_call import EnumsEthCall
from typing import List

class In3Core(object):

    in3 = None

    @staticmethod
    def init_in3():
        if In3Core.in3 is None:
            aux = libin3.new_in3p()
            libin3.init_client(aux)
            In3Core.in3 = aux

    @staticmethod
    def close():
        libin3.delete_in3p(In3Core.in3)
        In3Core.in3 = None

    def __init__(self):
        In3Core.init_in3()

    def in3_eth_blockNumber(self):
        return libin3.eth_blockNumber(In3Core.in3)

    def in3_raw_rpc(self, method: str, params:str):
        return libin3.in3_client_rpc_raw(self.in3,method,params)

