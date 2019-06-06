from src.modules.eth.block_transaction_count.block_transaction_count import BlockTransactionCount
from src.modules.eth.transaction.transaction import Transaction
from src.modules.eth.uncle.uncle import Uncle
from src.modules.eth.code.code import Code
from src.modules.eth.sign.sign import Sign
from src.modules.eth.balance.balance import Balance
from src.modules.eth.storage.storage import Storage
from src.modules.eth.gas.gas import Gas
# from src.modules.eth.filter.filter import Filter
# from src.modules.eth.logs.logs import Logs
from src.dto.transaction_dto import TransactionDTO
# from src.dto.call_dto import CallDTO
# from src.dto.filter_dto import FilterDTO
# from src.dto.log_filter_dto import LogFilterDTO
#
#
#
# from src.utils.Utils import Config
from src.enums.enums_block_status import EnumsBlockStatus
from src.core.in3_core import In3Core
from src.modules.eth.account.account import Account
from src.modules.eth.block.Block import Block
from src.domain.in3_number import In3Number
from src.domain.bytes_types import Bytes32, Bytes20

class Ethereum:

    def __init__(self, in3_core:In3Core ):
        self.__block = Block(in3_core)
        self.__account = Account(in3_core)
        self.__block_transaction_count = BlockTransactionCount(in3_core)
        self.__transaction = Transaction(in3_core)
        self.__uncle = Uncle(in3_core)
        self.__code = Code(in3_core)
        self.__sign = Sign(in3_core)
        self.__balance = Balance(in3_core)
        self.__storage = Storage(in3_core)
        self.__gas = Gas(in3_core)
        # self.__filter= Filter(in3_core)
        # self.__logs = Logs(in3_core)


    # Block services
    def block_number(self):
        return self.__block.number()

    def get_block_by_hash(self, hash:Bytes32, full=False):
        return self.__block.by_hash(hash,full)

    def get_block_by_number(self, number:[EnumsBlockStatus,In3Number], full=False):
        return self.__block.by_number(number=number, full=full)

    # Accounts services
    def accounts(self):
        return self.__account.all()

    # Gas services
    def gas_price(self):
        return self.__gas.price()

    def get_block_transaction_count_by_hash(self, hash:Bytes32):
        return self.__block_transaction_count.byHash(hash=hash)

    def get_block_transaction_count_by_number(self, number:[In3Number,EnumsBlockStatus]):
        return self.__block_transaction_count.byNumber(number=number)

    def get_balance(self, address:Bytes20, number:[In3Number, EnumsBlockStatus]):
        return self.__balance.of(address=address, number=number)

    #
    def get_storage_at(self, address:Bytes20, position:In3Number, number:EnumsBlockStatus):
        return self.__storage.at(address=address, position=position, block_number=number)
    #
    def get_transaction_count(self, address:Bytes20, number:[In3Number, EnumsBlockStatus]):
        return self.__transaction.count(address=address, number=number)
    #
    def get_uncle_count_by_block_hash(self, hash:Bytes32):
        return self.__uncle.count_by_blockhash(hash=hash)
    #
    def get_uncle_count_by_block_number(self, number:[In3Number, EnumsBlockStatus]):
        return self.__uncle.count_by_blocknumber(number=number)
    #
    def get_code(self, address:Bytes20, number:In3Number):
        return self.__code.by_address_and_number(address=address, number=number)
    #
    def sign(self, address:Bytes20, message):
        return self.__sign.byAddress(address, message)

    def send_transaction(self, transaction: TransactionDTO):
        return self.__transaction.send(transaction=transaction)
    #
    # def send_raw_transaction(self, data):
    #     return self.__transaction.send_raw(data=data)
    #
    # def call(self, call_dto: CallDTO, number):
    #     return self.__transaction.call(dto=call_dto, number=number)
    #
    # def estimate_gas(self, transaction:TransactionDTO):
    #     return self.__transaction.estimate(transaction=transaction)
    #
    #
    def get_transaction_by_hash(self, hash:Bytes32):
        return self.__transaction.by_hash(hash=hash)

    def get_transaction_by_block_hash_and_index(self, hash:Bytes32, index:In3Number):
        return self.__transaction.by_blockhash_and_index(blockhash=hash, index=index)
    #
    def get_transaction_by_block_number_and_index(self, number:Bytes32, index:In3Number):
        return self.__transaction.by_blocknumber_and_index(blocknumber=number, index=index)
    #
    def get_transaction_receipt(self, hash:Bytes32):
        return self.__transaction.receipt(hash=hash)
    #
    def pending_transactions(self):
        return self.__transaction.pending()
    #
    def get_uncle_by_block_hash_and_index(self, hash:Bytes32, index:In3Number):
        return self.__uncle.by_blockhash_and_index(hash=hash, index=index)
    #
    def get_uncle_by_block_number_and_index(self, number:In3Number, index:In3Number):
        return self.__uncle.by_blocknumber_and_index(number=number, index=index)
    #
    # def new_filter(self, filter_dto: FilterDTO):
    #     return self.__filter.create(filter_dto=filter_dto)
    #
    # def new_block_filter(self):
    #     return self.__filter.block_create()
    #
    # def new_pending_transaction_filter(self):
    #     return self.__filter.pending_transaction_create()
    #
    # def uninstall_filter(self, filter_id):
    #     return self.__filter.uninstall(filter_id=filter_id)
    #
    # def get_filter_changes(self, filter_id):
    #     return self.__logs.filter_changes(filter_id)
    #
    # def get_logs_filter_logs(self,filter_id):
    #     return self.__logs.filter_id(filter_id=filter_id)
    #
    # def get_logs(self, log_filter:LogFilterDTO):
    #     return self.__logs.filter(filter=log_filter)



