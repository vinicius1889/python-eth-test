import unittest
from rpc.eth.ethereum import Ethereum
from rpc.eth.enums.enums_execution_type import EnumsExecutionType
from rpc.eth.enums.enums_block_status import EnumsBlockStatus
from dto.transaction_dto import TransactionDTO
from dto.call_dto import CallDTO
from dto.filter_dto import FilterDTO
from dto.log_filter_dto import LogFilterDTO


class EthereumTestCase(unittest.TestCase):

    def test_block_number(self):
        eth = Ethereum(EnumsExecutionType.RPC_DIRECT)
        number = eth.block.number()
        self.assertEqual(number['id'], 1)

    def test_block_by_hash(self):
        eth = Ethereum(EnumsExecutionType.MOCK)
        number = eth.block.by_hash()
        self.assertEqual(number['id'], 1)

    def test_block_by_number(self):
        eth = Ethereum(EnumsExecutionType.RPC_DIRECT)
        number = eth.block.by_number("0xb2549a", full=False)
        self.assertEqual(number['id'], 1)

    def test_block_by_number_using_enum_status_latest(self):
        eth = Ethereum(EnumsExecutionType.RPC_DIRECT)
        number = eth.block.by_number(EnumsBlockStatus.LATEST, full=False)
        self.assertEqual(number['id'], 1)

    def test_block_transaction_count_by_number(self):
        eth =  Ethereum(EnumsExecutionType.RPC_DIRECT)
        number = eth.block_transaction_count.byNumber(EnumsBlockStatus.LATEST)
        self.assertEqual(number['id'],1)

    def test_transaction_by_hash(self):
        eth =  Ethereum(EnumsExecutionType.MOCK)
        number = eth.transaction.by_hash("MY_HASH_HERE")
        self.assertEqual(number['result']['transactionIndex'],"0x41")

    def test_transaction_by_blockhash_and_index(self):
        eth = Ethereum(EnumsExecutionType.MOCK)
        number = eth.transaction.by_blockhash_and_index("MY_HASH")
        self.assertEqual(number['result']['transactionIndex'],"0x41")

    def test_transaction_by_blocknumber_and_index(self):
        eth =  Ethereum(EnumsExecutionType.MOCK)
        number = eth.transaction.by_blocknumber_and_index(EnumsBlockStatus.LATEST)
        self.assertEqual(number['result']['transactionIndex'],"0x41")


    def test_transaction_receipt(self):
        eth = Ethereum(EnumsExecutionType.MOCK)
        number = eth.transaction.receipt("MY_HASH")
        self.assertEqual(number['result']['transactionIndex'],"0x1")

    def test_transaction_pending(self):
        eth = Ethereum(EnumsExecutionType.MOCK)
        number = eth.transaction.pending("MY_HASH")
        self.assertEqual(len(number['result']), 2)


    def test_transaction_count(self):
        eth = Ethereum(EnumsExecutionType.MOCK)
        address = "address"
        number = eth.transaction.count(address,EnumsBlockStatus.LATEST)
        self.assertEqual(number['id'], 1)


    def test_uncle_count_by_block_hash(self):
        eth = Ethereum(EnumsExecutionType.MOCK)
        hash = "hash"
        number = eth.uncle.countByBlockHash(hash)
        self.assertEqual(number['id'], 1)

    def test_uncle_count_by_block_number(self):
        eth = Ethereum(EnumsExecutionType.RPC_DIRECT)
        number = eth.uncle.countByBlockNumber(number=EnumsBlockStatus.LATEST)
        self.assertEqual(number['id'], 1)

    def test_uncle_by_block_hash_and_index(self):
        eth = Ethereum(EnumsExecutionType.MOCK)
        hash = "hash"
        index= "0x0"
        number = eth.uncle.byBlockHashAndIndex(hash,index)
        self.assertEqual(number['id'], 1)

    def test_uncle_by_block_number_and_index(self):
        eth = Ethereum(EnumsExecutionType.MOCK)
        number = EnumsBlockStatus.LATEST
        index = "0x0"
        number = eth.uncle.byBlockNumberAndIndex(number, index)
        self.assertEqual(number['id'], 1)

    def test_get_code_by_address_and_number(self):
        eth = Ethereum(EnumsExecutionType.MOCK)
        number = EnumsBlockStatus.LATEST
        address = "0x0"
        number = eth.code.byAddressAndBlockNumber(address, number)
        self.assertEqual(number['id'], 1)

    def test_sign_by_address(self):
        eth = Ethereum(EnumsExecutionType.MOCK)
        address = "0x0"
        message = "0xdeadbeaf"
        number = eth.sign.byAddress(address, message)
        self.assertEqual(number['id'], 1)


    def test_transaction_send(self):
        eth = Ethereum(EnumsExecutionType.MOCK)
        transactionDTO = TransactionDTO(From="0xb60e8dd61c5d32be8058bb8eb970870f07233155",
                       to="0xd46e8dd67c5d32be8058bb8eb970870f07244567",
                       data="0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675",
                       gas="0x76c0",
                       gasPrice="0x9184e72a000",
                       value="0x9184e72a"
                       )
        number = eth.transaction.send(transactionDTO)
        self.assertEqual(number['id'], 1)

    def test_transaction_call(self):
        eth = Ethereum(EnumsExecutionType.MOCK)
        dto = CallDTO(From="0xb60e8dd61c5d32be8058bb8eb970870f07233155",
                       to="0xd46e8dd67c5d32be8058bb8eb970870f07244567",
                       data="0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675",
                       gas="0x76c0",
                       gasPrice="0x9184e72a000",
                       value="0x9184e72a"
                       )
        number = eth.transaction.call(dto, EnumsBlockStatus.LATEST)
        self.assertEqual(number['id'], 1)

    def test_transaction_estimate(self):
        eth = Ethereum(EnumsExecutionType.MOCK)
        dto = TransactionDTO(From="0xb60e8dd61c5d32be8058bb8eb970870f07233155",
                       to="0xd46e8dd67c5d32be8058bb8eb970870f07244567",
                       data="0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675",
                       gas="0x76c0",
                       gasPrice="0x9184e72a000",
                       value="0x9184e72a"
                       )
        number = eth.transaction.estimate(dto)
        self.assertEqual(number['id'], 1)

    def test_get_all_accounts(self):
        eth = Ethereum(execution_type=EnumsExecutionType.RPC_DIRECT)
        accounts = eth.account.all()
        self.assertEqual(accounts['id'], 1)

    def test_balance_of(self):
        eth = Ethereum(execution_type=EnumsExecutionType.RPC_DIRECT)
        address="0x633ee843d1f4170cfcc60ec119b4fb2d68e5545e"
        accounts = eth.balance.of(address, EnumsBlockStatus.LATEST)
        self.assertEqual(accounts['id'], 1)

    def test_storage_at(self):
        eth = Ethereum(execution_type=EnumsExecutionType.RPC_DIRECT)
        address="0x633ee843d1f4170cfcc60ec119b4fb2d68e5545e"
        position = "0x0"
        storage = eth.storage.at(address,position, EnumsBlockStatus.LATEST)
        self.assertEqual(storage['id'], 1)

    def test_gas_price(self):
        eth = Ethereum(execution_type=EnumsExecutionType.RPC_DIRECT)
        price = eth.gas.price()
        self.assertEqual(price['id'], 1)

    def test_new_filter(self):
        eth = Ethereum(execution_type=EnumsExecutionType.MOCK)
        dto = FilterDTO.build_from_block("0x01")
        filter = eth.filter.create(dto)
        self.assertEqual(filter['id'], 1)

    def test_new_block_filter(self):
        eth = Ethereum(execution_type=EnumsExecutionType.MOCK)
        filter = eth.filter.block_create()
        self.assertEqual(filter['id'], 1)

    def test_new_pending_transaction_filter(self):
        eth = Ethereum(execution_type=EnumsExecutionType.MOCK)
        filter = eth.filter.pending_transaction_create()
        self.assertEqual(filter['id'], 1)

    def test_uninstall_filter(self):
        eth = Ethereum(execution_type=EnumsExecutionType.MOCK)
        # id = eth.filter.pending_transaction_create()['result']
        id = "0x8"
        filter = eth.filter.uninstall(id)
        self.assertEqual(filter['result'], True)

    def test_log_filter_changes(self):
        eth = Ethereum(execution_type=EnumsExecutionType.MOCK)
        id="0x1"
        log = eth.logs.filter_changes(id)
        self.assertEqual(log['id'], 1)

    def test_log_filter_by_id(self):
        eth = Ethereum(execution_type=EnumsExecutionType.MOCK)
        id = "0x1"
        log = eth.logs.filter_id(id)
        self.assertEqual(log['id'], 1)

    def test_log_filter_by_filter_object(self):
        eth = Ethereum(execution_type=EnumsExecutionType.MOCK)
        aux = FilterDTO.build_from_block("0x0001")
        dto = LogFilterDTO.build_by_filter_dto(aux)
        log = eth.logs.filter(dto)
        self.assertEqual(log['id'], 1)
