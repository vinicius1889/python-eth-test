from unittest import TestCase
from src.core.slib import libin3


class LibTestsCase(TestCase):

    BLOCK_NUMBER = 6970454

    def test_create_in3_pointer(self):
        in3_p = libin3.new_in3p()
        self.assertIsNotNone(in3_p)
        libin3.delete_in3p(in3_p)

    def test_implement_new_in3p(self):
        in3_p = libin3.new_in3p()
        libin3.init_client(in3_p)
        self.assertEqual(1,in3_p.chainId)
        libin3.delete_in3p(in3_p)

    def test_block_number(self):
        in3p = libin3.new_in3p()
        libin3.init_client(in3p)
        num = libin3.eth_blockNumber(in3p)
        self.assertIsNotNone(num)
        libin3.delete_in3p(in3p)

    def test_get_block_by_number_directly(self):
        in3p = libin3.new_in3p()
        libin3.init_client(in3p)
        block = libin3.eth_getBlockByNumber(in3p, LibTestsCase.BLOCK_NUMBER, False)
        self.assertEqual(LibTestsCase.BLOCK_NUMBER, block.number)
        libin3.delete_in3p(in3p)




