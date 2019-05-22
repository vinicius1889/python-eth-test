from unittest import TestCase
from src.in3_client import In3Client


class In3ClientTestCase(TestCase):


    def test_get_block_number(self):
        in3 = In3Client()
        block_number = in3.eth.block_number()
        self.assertTrue(block_number>0)


    def test_get_block_by_number(self):
        in3 = In3Client()
        number = int("0x6a5c56",16)
        full = False
        block = in3.eth.get_block_by_number(number, full)
        self.assertEqual(number,block.number)

    def test_get_block_by_hash(self):
        in3 = In3Client()
        hash = 0x4c45aaaf983de4bd6cd81fb0a63f93d1eed148242e1a08fe477d4803d9181372
        full = False
        block = in3.eth.get_block_by_hash(hash, full)
        self.assertIsNotNone(block)

    def test_get_gas_price(self):
        in3 = In3Client()
        price = in3.eth.gas_price()
        self.assertIsNotNone(price)