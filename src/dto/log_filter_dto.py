from src.dto.filter_dto import FilterDTO


class LogFilterDTO(FilterDTO):

    def __init__(self):
        super().__init__()
        self.blockHash = None

    @classmethod
    def build_by_filter_dto(cls,filter_dto):
        dto = LogFilterDTO()
        dto.__dict__.update(filter_dto.__dict__)
        return dto


