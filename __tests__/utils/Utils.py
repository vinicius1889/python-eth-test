import unittest
from  utils.Utils import RPC
from rpc.eth.enums.enums_eth_call import EnumsEthCall
from rpc.eth.enums.enums_rpc_chains import EnumsRPCChains


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

