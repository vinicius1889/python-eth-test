from src.core.slib import libin3


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

    def in3_eth_get_block_by_hash(self, hash, full=False):
        aux = libin3.uint8_tp_value(hash)
        return libin3.eth_getBlockByHash(In3Core.in3, aux, full)

    def in3_eth_get_block_by_number(self, number,full=False):
        return libin3.eth_getBlockByNumber(In3Core.in3, number, full)

    def in3_eth_get_gas_price(self):
        return libin3.eth_gasPrice(In3Core.in3)

