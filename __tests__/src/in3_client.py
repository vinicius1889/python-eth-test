from unittest import TestCase
from src.in3_client import In3Client
from src.enums.enums_eth_call import EnumsEthCall
import json
from enum import Enum

class In3ClientTestCase(TestCase):


    def test_ethereum_instance_is_not_null(self):
        in3 = In3Client()
        self.assertIsNotNone(in3)


    def test_json(self):
        params = ["0x123", True]
        string = json.dumps(params)
        print(string)
        print(type(EnumsEthCall.RPC_GAS_PRICE))
        print(isinstance(EnumsEthCall.RPC_GAS_PRICE, Enum))
        aux = EnumsEthCall.RPC_GAS_PRICE



    def test_get_block_number(self):
        in3 = In3Client()
        block_number = in3.eth.block_number()
        self.assertTrue(block_number>0)



    #
    #
    # def test_get_block_by_number(self):
    #     in3 = In3Client()
    #     number = int("0x6a5c56",16)
    #     full = False
    #     block = in3.eth.get_block_by_number(number, full)
    #     self.assertEqual(number,block.number)
    #
    # def test_get_block_by_hash(self):
    #     in3 = In3Client()
    #     hash = 0x4c45aaaf983de4bd6cd81fb0a63f93d1eed148242e1a08fe477d4803d9181372
    #     full = False
    #     block = in3.eth.get_block_by_hash(hash, full)
    #     self.assertIsNotNone(block)
    #
    # def test_get_gas_price(self):
    #     in3 = In3Client()
    #     price = in3.eth.gas_price()
    #     self.assertIsNotNone(price)
    #
    # def test_get_balance(self):
    #     in3 = In3Client()
