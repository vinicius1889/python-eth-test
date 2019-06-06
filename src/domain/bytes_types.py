from abc import abstractmethod


class BytesT:

    def __init__(self, data:str):
        self.__validate(data)
        self.set_data(data)

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    @abstractmethod
    def __validate(self, data):
        pass

    def get_hash_without_0x(self):
        return self.get_data()[2:]


class Bytes32(BytesT):

    def __init__(self, data: str):
        super().__init__( data)

    def __validate(self, data):
        if len(data) is not 66:
            raise Exception('Invalid hash')




class Bytes20(BytesT):

    def __init__(self, data:str):
        super().__init__(data)

    def __validate(self, data):
        if len(data) is not 42:
            raise Exception('Invalid hash length')

