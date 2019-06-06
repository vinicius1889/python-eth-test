import unittest
from src.modules.eth.ethereum import Ethereum
from src.enums.enums_block_status import EnumsBlockStatus
from src.core.in3_core import In3Core
import json
from src.domain.in3_number import In3Number
from src.domain.bytes_types import Bytes32,Bytes20
from src.dto.transaction_dto import TransactionDTO


class EthereumTestCase(unittest.TestCase):


    def get_in3_core(self):
        instance =  In3Core()
        return Ethereum(instance)

    # block ethereum functions
    def test_block_number(self):
        self.assertIsNotNone(self.get_in3_core().block_number())

    def test_block_by_hash(self):
        eth = self.get_in3_core()
        hash = Bytes32('0xdcded60b27fc1fc3987e9416cb3dd81159552426ab6e027a308ea94985a7f258')
        number = eth.get_block_by_hash(hash,False)
        print(number)

    def test_block_by_number(self):
        eth = self.get_in3_core()
        num = In3Number(0x6a5c56)
        block = eth.get_block_by_number(num, full=False)
        self.assertIsNotNone(block["author"])

    def test_block_by_number_by_enum_status_latest(self):
        eth = self.get_in3_core()
        block = eth.get_block_by_number(EnumsBlockStatus.LATEST, full=False)
        self.assertIsNotNone(block["author"])
    # end of block ethereum functions

    # Testing accounts
    def test_get_all_accounts_if_it_works_without_test_any_account(self):
        eth = self.get_in3_core()
        accounts = eth.accounts()
        self.assertIsNotNone(accounts)

    # gas price
    def test_gas_price(self):
        eth = self.get_in3_core()
        price = eth.gas_price()
        self.assertIsNotNone(price)


    #TODO test c client here
    def test_block_transaction_count_by_number(self):
        eth = self.get_in3_core()
        result = eth.get_block_transaction_count_by_number(EnumsBlockStatus.LATEST)
        print(result)

    #TODO test c client here
    def test_block_transaction_count_by_hash(self):
        eth = self.get_in3_core()
        hash = Bytes32('0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238')
        result = eth.get_block_transaction_count_by_hash(hash)
        print(result)

    def test_balance_of(self):
        eth = self.get_in3_core()
        bytes20 = Bytes20('0x633ee843d1f4170cfcc60ec119b4fb2d68e5545e')
        balance = eth.get_balance(bytes20, EnumsBlockStatus.LATEST)
        self.assertEqual('0x0', balance)

    #TODO Finish the transaction function
    def test_transaction_send(self):
        eth = self.get_in3_core()
        transactionDTO = TransactionDTO(From="0xb60e8dd61c5d32be8058bb8eb970870f07233155",
                       to="0xd46e8dd67c5d32be8058bb8eb970870f07244567",
                       data="0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675",
                       gas="0x76c0",
                       gasPrice="0x9184e72a000",
                       value="0x9184e72a"
                       )
        number = eth.send_transaction(transactionDTO)
        self.assertIsNotNone(number)


    #TODO validate this test
    def test_transaction_by_hash(self):
        eth =  self.get_in3_core()
        address = Bytes32('0x88df016429689c079f3b2f6ad39fa052532c56795b733da78a91ebe6a713944b')
        transaction = eth.get_transaction_by_hash(address)
        print(transaction)


    #TODO validate
    def test_transaction_by_blockhash_and_index(self):
        eth = self.get_in3_core()
        block_hash = Bytes32('0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331')
        num = In3Number(0x0)
        result = eth.get_transaction_by_block_hash_and_index(block_hash, num)
        print(result)

    #TODO validate
    def test_transaction_by_blocknumber_and_index(self):
        eth = self.get_in3_core()
        number = In3Number(0x29c)
        index = In3Number(0x0)
        result = eth.get_transaction_by_block_number_and_index(number, index)
        print(result)

    #TODO validate
    def test_transaction_receipt(self):
        eth = self.get_in3_core()
        result = eth.get_transaction_receipt(Bytes32('0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238'))

    #TODO document
    def test_transaction_pending(self):
        eth = self.get_in3_core()
        result = eth.pending_transactions()
        print(result)


    def test_uncle_count_by_block_hash(self):
        eth = self.get_in3_core()
        hash = Bytes32('0xc94770007dda54cF92009BFF0dE90c06F603a09f')
        number = eth.get_uncle_count_by_block_hash(hash)
        print(number)

    def test_uncle_count_by_block_number(self):
        eth = self.get_in3_core()
        block = eth.get_uncle_count_by_block_number(EnumsBlockStatus.LATEST)
        print(block)

    def test_uncle_by_block_hash_and_index(self):
        eth = self.get_in3_core()
        hash = Bytes32('0xc6ef2fc5426d6ad6fd9e2a26abeab0aa2411b7ab17f30a99d3cb96aed1d1055b')
        index= In3Number(0x0)
        number = eth.get_uncle_by_block_hash_and_index(hash, index)
        print(number)

    #TODO
    def test_uncle_by_block_number_and_index(self):
        eth = self.get_in3_core()
        number = In3Number(0x29c)
        index = In3Number(0x0)
        number = eth.get_uncle_by_block_number_and_index(number, index)
        print(number)

    def test_get_code_by_address_and_number(self):
        eth = self.get_in3_core()
        address = Bytes20('0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b')
        number = In3Number(0x0)
        code = eth.get_code(address, number)

    def test_transaction_count(self):
        eth = self.get_in3_core()
        address = Bytes20('0xc94770007dda54cF92009BFF0dE90c06F603a09f')
        number  = eth.get_transaction_count(address,EnumsBlockStatus.LATEST)
        self.assertEqual('0x208', number)

    def test_sign_by_address(self):
        eth = self.get_in3_core()
        address = Bytes20('0x9b2055d370f73ec7d8a03e965129118dc8f5bf83')
        message = '0xdeadbeaf'
        eth.sign(address,message)
    #
    #
    #
    # def test_transaction_call(self):
    #     eth = Ethereum(EnumsExecutionType.MOCK)
    #     dto = CallDTO(From="0xb60e8dd61c5d32be8058bb8eb970870f07233155",
    #                    to="0xd46e8dd67c5d32be8058bb8eb970870f07244567",
    #                    data="0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675",
    #                    gas="0x76c0",
    #                    gasPrice="0x9184e72a000",
    #                    value="0x9184e72a"
    #                    )
    #     number = eth.__transaction.call(dto, EnumsBlockStatus.LATEST)
    #     self.assertEqual(number['id'], 1)
    #
    # def test_transaction_estimate(self):
    #     eth = Ethereum(EnumsExecutionType.MOCK)
    #     dto = TransactionDTO(From="0xb60e8dd61c5d32be8058bb8eb970870f07233155",
    #                    to="0xd46e8dd67c5d32be8058bb8eb970870f07244567",
    #                    data="0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675",
    #                    gas="0x76c0",
    #                    gasPrice="0x9184e72a000",
    #                    value="0x9184e72a"
    #                    )
    #     number = eth.__transaction.estimate(dto)
    #     self.assertEqual(number['id'], 1)
    #

    #
    #
    def test_storage_at(self):
        eth = self.get_in3_core()
        address = Bytes20('0x295a70b2de5e3953354a6a8344e616ed314d7251')
        position = In3Number(0x0)
        storage = eth.get_storage_at(address, position, EnumsBlockStatus.LATEST)
    #

    #
    # def test_new_filter(self):
    #     eth = Ethereum(execution_type=EnumsExecutionType.MOCK)
    #     dto = FilterDTO.build_from_block("0x01")
    #     filter = eth.__filter.create(dto)
    #     self.assertEqual(filter['id'], 1)
    #
    # def test_new_block_filter(self):
    #     eth = Ethereum(execution_type=EnumsExecutionType.MOCK)
    #     filter = eth.__filter.block_create()
    #     self.assertEqual(filter['id'], 1)
    #
    # def test_new_pending_transaction_filter(self):
    #     eth = Ethereum(execution_type=EnumsExecutionType.MOCK)
    #     filter = eth.__filter.pending_transaction_create()
    #     self.assertEqual(filter['id'], 1)
    #
    # def test_uninstall_filter(self):
    #     eth = Ethereum(execution_type=EnumsExecutionType.MOCK)
    #     # id = eth.filter.pending_transaction_create()['result']
    #     id = "0x8"
    #     filter = eth.__filter.uninstall(id)
    #     self.assertEqual(filter['result'], True)
    #
    # def test_log_filter_changes(self):
    #     eth = Ethereum(execution_type=EnumsExecutionType.MOCK)
    #     id="0x1"
    #     log = eth.__logs.filter_changes(id)
    #     self.assertEqual(log['id'], 1)
    #
    # def test_log_filter_by_id(self):
    #     eth = Ethereum(execution_type=EnumsExecutionType.MOCK)
    #     id = "0x1"
    #     log = eth.__logs.filter_id(id)
    #     self.assertEqual(log['id'], 1)
    #
    # def test_log_filter_by_filter_object(self):
    #     eth = Ethereum(execution_type=EnumsExecutionType.MOCK)
    #     aux = FilterDTO.build_from_block("0x0001")
    #     dto = LogFilterDTO.build_by_filter_dto(aux)
    #     log = eth.__logs.filter(dto)
    #     self.assertEqual(log['id'], 1)
