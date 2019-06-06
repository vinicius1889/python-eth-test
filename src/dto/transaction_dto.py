import json
from src.domain.bytes_types import Bytes20
from src.domain.in3_number import In3Number

class TransactionDTO(object):


    def __init__(self,From, to, data, gas=None, gasPrice=None, value=None, nonce=None ):
        self.__from = From
        self.__to = to
        self.__gas = gas
        self.__gasPrice = gasPrice
        self.__value = value
        self.__data = data
        self.__nonce = nonce


    def set_gas(self,gas:In3Number):
        self.__gas = gas.to_hex()

    def set_gas_price(self, gas_price:In3Number):
        self.__gasPrice = gas_price.to_hex()

    def set_value(self, value:In3Number):
        self.__value = value.to_hex()

    def set_nonce(self, nonce:In3Number):
        self.__nonce = nonce.to_hex()

    @staticmethod
    def create_from_types(From:Bytes20, to:Bytes20, data:str):
        return TransactionDTO(From.get_data(), to.get_data(), data)



    def toJson(self):

        aux = self.__dict__
        result = {}
        for d in aux:
            name = d.split('__').pop()
            result[name] = aux[d]

        return json.dumps(result)



# dto = TransactionDTO("0x123123131", "0x123131231321", "dsadadadada")


