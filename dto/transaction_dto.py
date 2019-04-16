import json


class TransactionDTO(object):


    def __init__(self,From, to, data, gas=None, gasPrice=None, value=None, nonce=None ):
        self.From = From
        self.to = to
        self.gas = gas
        self.gasPrice = gasPrice
        self.value = value
        self.data = data
        self.nonce = nonce

    def toJson(self):
        aux = self.__dict__
        result = {}
        for d in aux:
            name = d[0].lower()+d[1:]
            result[name] = aux[d]

        return json.dumps(result)



# dto = TransactionDTO("0x123123131", "0x123131231321", "dsadadadada")


