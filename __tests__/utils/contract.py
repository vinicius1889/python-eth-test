from unittest import TestCase
from utils.contract.contract import ContractUtils

class ContractUtilTestcase(TestCase):

    def testing_signature_contract_call(self):
        signature = "baz(uint32,bool)"
        result_expected = "0xcdcd77c000000000000000000000000000000000000000000000000000000000000000450000000000000000000000000000000000000000000000000000000000000001"
        params = []
        params.append(69)
        params.append(True)

        result = ContractUtils().signature_hash_call(signature, params, "0x")

        self.assertEqual(result,result_expected)


    def testing_signature_contract_call_2(self):
        signature = "bar(bytes3[2])"
        result_expected = "0xfce353f661626300000000000000000000000000000000000000000000000000000000006465660000000000000000000000000000000000000000000000000000000000"
        params = []
        params.append("abc")
        params.append("def")

        result = ContractUtils().signature_hash_call(signature, params, "0x")

        self.assertEqual(result,result_expected)


    def testing_signature_contract_call_3(self):

        # uint to uint256
        #  "1234567890", "Hello, world!"
        signature = "f(uint,uint32[],bytes10,bytes)"
        result_expected = "0x8be65246\
0000000000000000000000000000000000000000000000000000000000000123\
0000000000000000000000000000000000000000000000000000000000000080\
3132333435363738393000000000000000000000000000000000000000000000\
00000000000000000000000000000000000000000000000000000000000000e0\
0000000000000000000000000000000000000000000000000000000000000002\
0000000000000000000000000000000000000000000000000000000000000456\
0000000000000000000000000000000000000000000000000000000000000789\
000000000000000000000000000000000000000000000000000000000000000d\
48656c6c6f2c20776f726c642100000000000000000000000000000000000000"
        params = []
        params.append(0x123)
        params.append([0x456, 0x789])
        params.append("1234567890")
        params.append("Hello, world!")


        result = ContractUtils().signature_hash_call_with_dynamic_types(signature, params, "0x")

        self.assertEqual(result_expected,result)




    def test_calling_array(self):
        p = [0x456, 0x789]
        res = ContractUtils().getHexValue(p)
        result = ("".join(res))
        self.assertEqual("00000000000000000000000000000000000000000000000000000000000004560000000000000000000000000000000000000000000000000000000000000789",result)

