import json

class CallDTO(object):

    def __init__(self,to,  From=None, gas=None, gasPrice=None, value=None, data=None ):
        self .to = to
        self.From = From
        self.gas  = gas
        self.gasPrice = gasPrice
        self.value = value
        self.data = data

    def toJson(self):
        aux = self.__dict__
        result = {}
        for d in aux:
            name = d[0].lower()+d[1:]
            result[name] = aux[d]

        return json.dumps(result)

