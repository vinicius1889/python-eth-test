import unittest
from src.utils.Utils import RPC
from src.utils.Utils import Hex
from src.utils.Utils import Hash
from src.enums.enums_eth_call import EnumsEthCall
from src.enums.enums_rpc_chains import EnumsRPCChains


class UtilsTestCase(unittest.TestCase):

    def testingNothingYet(self):
        pass


class UtilRPC(unittest.TestCase):

    def testing_call_with_normal_id(self):
        response = RPC().call(method=EnumsEthCall.RPC_BLOCK_NUMBER.value)
        self.assertEqual(response['id'],1)

    def testing_call_with_custom_id(self):
        CUSTOM_ID = 123
        response = RPC().call(method=EnumsEthCall.RPC_BLOCK_NUMBER.value, params=[], url=EnumsRPCChains.TOBALABA.value, id=CUSTOM_ID)
        self.assertEqual(response['id'],CUSTOM_ID)


    def testing(self):
        name = EnumsEthCall.RPC_BLOCK_BY_NUMBER

        print(isinstance(name, EnumsEthCall))


class HexTestCase(unittest.TestCase):

    STRING_TO_BE_TESTED="SLOCKIT"
    INTEGER_TO_BE_TESTED=16
    HEXA_TO_BE_TESTED="0xa"


    def testing_string_to_hex(self):
        hexa_result = Hex.from_string_to_hex(HexTestCase.STRING_TO_BE_TESTED)
        string_result = Hex.to_string(hexa_result)
        self.assertEqual(string_result,HexTestCase.STRING_TO_BE_TESTED)

    def testing_interger(self):
        hexa_result = Hex.from_int_to_hex(HexTestCase.INTEGER_TO_BE_TESTED)
        int_result = Hex.to_int(hexa_result)
        self.assertEqual(int_result, HexTestCase.INTEGER_TO_BE_TESTED)

    def testing_hexa(self):
        self.assertEqual(Hex.to_int(HexTestCase.HEXA_TO_BE_TESTED), 10)

    def testing_hexa_starting_with_x(self):
        hex_with_x="0x736c6f636b6974"
        slockit = Hex.to_string(hex_with_x)
        self.assertEqual(slockit, "slockit")

    def testing_string(self):
        string = "abc"
        result = (Hex.from_string_to_hex(string,32))
        result_expected="6162630000000000000000000000000000000000000000000000000000000000"
        self.assertEqual(result_expected, result)



class HashTestCase(unittest.TestCase):

    SIGNATURE_EXAMPLE="baz(uint32,bool)"

    def test_signature_keccak(self):
        result = Hash.keccak(HashTestCase.SIGNATURE_EXAMPLE, 4)
        self.assertEqual(result, "cdcd77c0")

    def test_signature_keccak_full(self):
        result = Hash.keccak(HashTestCase.SIGNATURE_EXAMPLE)
        self.assertEqual(result, "cdcd77c0992ec5bbfc459984220f8c45084cc24d9b6efed1fae540db8de801d2")





