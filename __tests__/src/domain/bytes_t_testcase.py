from unittest import TestCase
from src.domain.bytes_types import Bytes32, Bytes20


class Bytes32TestCase(TestCase):

    def test_basic_bytes32(self):
        bytes32 = Bytes32('0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238')
        self.assertEqual('0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238', bytes32.get_data())

    def test_basic_bytes32_without_0x(self):
        bytes32 = Bytes32('0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238')
        self.assertEqual('b903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238', bytes32.get_hash_without_0x())

    def test(self):
        Bytes32('0xc5bcb31100d8993fd46a219770545841a64aa7e5076000d5ad81524a8217351b')


class Bytes20TestCase(TestCase):

    def test_basic20(self):
        bytes20 = Bytes20('0xb60e8dd61c5d32be8058bb8eb970870f07233155')
        self.assertEqual('0xb60e8dd61c5d32be8058bb8eb970870f07233155', bytes20.get_data())


    def test_basic_bytes20_without_0x(self):
        bytes20 = Bytes20('0xb60e8dd61c5d32be8058bb8eb970870f07233155')
        self.assertEqual('b60e8dd61c5d32be8058bb8eb970870f07233155', bytes20.get_hash_without_0x())


