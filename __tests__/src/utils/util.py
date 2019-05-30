from unittest import TestCase
from src.enums.enums_block_status import EnumsBlockStatus
from src.utils.Utils import params_to_json_string

class UtilsTestCase(TestCase):

    def testing_params_object_to_json_string(self):
        params = []
        params.append("0x123123213131")
        params.append(True)
        params.append(EnumsBlockStatus.LATEST)
        string = params_to_json_string(params)
        self.assertEqual('["0x123123213131", true, "latest"]', string)

