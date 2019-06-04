from unittest import TestCase
from src.domain.in3_number import In3Number

class In3NumberTestCase(TestCase):

    def test_integer_to_hex(self):
        in3_number = In3Number(10000000000000)
        self.assertEqual('0x9184e72a000', in3_number.to_hex())

    def test_hexa_to_integer(self):
        in3_number = In3Number('0x9184e72a000')
        self.assertEqual(10000000000000, in3_number.to_int())

    def testing_158972490234375000_to_hex(self):
        in3_number = In3Number(158972490234375000)
        self.assertEqual('0x234c8a3397aab58', in3_number.to_hex())


