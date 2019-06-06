from unittest import TestCase
from src.dto.transaction_dto import TransactionDTO
from src.domain.bytes_types import Bytes20
from src.domain.in3_number import In3Number



class TransactionDTOTestCase(TestCase):

    JSON_STR = '{"from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155", "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567", "gas": "0x76c0", "gasPrice": "0x9184e72a000", "value": "0x9184e72a", "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675", "nonce": null}'

    def test_transaction_dto_basic(self):
        transactionDTO = TransactionDTO(From="0xb60e8dd61c5d32be8058bb8eb970870f07233155",
                                        to="0xd46e8dd67c5d32be8058bb8eb970870f07244567",
                                        data="0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675",
                                        gas="0x76c0",
                                        gasPrice="0x9184e72a000",
                                        value="0x9184e72a"
                                        )
        self.assertEqual(TransactionDTOTestCase.JSON_STR, transactionDTO.toJson())


    def test_transaction_dto_obj(self):
        data = '0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675'
        transaction = TransactionDTO.create_from_types(From=Bytes20('0xb60e8dd61c5d32be8058bb8eb970870f07233155'),
                                                       to=Bytes20('0xd46e8dd67c5d32be8058bb8eb970870f07244567'),
                                                       data= data)
        transaction.set_gas(In3Number(0x76c0))
        transaction.set_gas_price(In3Number(0x9184e72a000))
        transaction.set_value(In3Number(0x9184e72a))
        self.assertEqual(TransactionDTOTestCase.JSON_STR, transaction.toJson())

