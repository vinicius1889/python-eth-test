class In3Number:

    def __init__(self, number):
        if isinstance(number,str):
            number = int(number, 16)

        self.__number = number

    def to_hex(self) -> str:
        return hex(self.__number)

    def to_int(self) -> int:
        return self.__number

    
