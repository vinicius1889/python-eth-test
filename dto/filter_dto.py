import json
from  rpc.eth.enums.enums_block_status import EnumsBlockStatus

class FilterDTO:

    def __init__(self):
        self.fromBlock = None
        self.toBlock = None
        self.address = None
        self.topic = None


    @staticmethod
    def build_from_block(from_block):
        dto = FilterDTO()
        dto.fromBlock = from_block
        return dto

    @staticmethod
    def build_from_block_and_address(from_block, address):
        dto = FilterDTO()
        dto.fromBlock = from_block
        dto.address = address
        return dto

    def to_json(self, skip_null=False):
        aux = self.__dict__
        dict = {}
        for d in aux:
            dict[d] = aux[d]
            if isinstance(aux[d], EnumsBlockStatus):
                dict[d] = aux[d].value

        if not skip_null:
            return json.dumps(dict)

        not_null_dict={}
        for d in dict:
            if dict[d] is not None:
                not_null_dict[d] = dict[d]
        return json.dumps(not_null_dict)





