import src.modules.eth.block.Block as bl
from src.modules.eth.block_transaction_count.block_transaction_count import BlockTransactionCount
from src.modules.eth.transaction.transaction import Transaction
from src.modules.eth.uncle.uncle import Uncle
from src.modules.eth.code.code import Code
from src.modules.eth.sign.sign import Sign
from src.modules.eth.account.account import Account
from src.modules.eth.balance.balance import Balance
from src.modules.eth.storage.storage import Storage
from src.modules.eth.gas.gas import Gas
from src.modules.eth.filter.filter import Filter
from src.modules.eth.logs.logs import Logs
from src.dto.transaction_dto import TransactionDTO
from src.dto.call_dto import CallDTO
from src.dto.filter_dto import FilterDTO
from src.dto.log_filter_dto import LogFilterDTO



from src.utils.Utils import Config
from src.enums.enums_execution_type import EnumsExecutionType


class Ethereum(object):

    def __init__(self, execution_type=EnumsExecutionType.NORMAL):
        Config.execution_type = execution_type
        self.__block = bl.Block(execution_type)
        self.__block_transaction_count = BlockTransactionCount(execution_type)
        self.__transaction = Transaction(execution_type)
        self.__uncle = Uncle(execution_type)
        self.__code = Code(execution_type)
        self.__sign = Sign(execution_type)
        self.__account = Account(execution_type)
        self.__balance = Balance(execution_type)
        self.__storage = Storage(execution_type)
        self.__gas = Gas(execution_type)
        self.__filter= Filter(execution_type)
        self.__logs = Logs(execution_type)


    def gas_price(self):
        return self.__gas.price()

    def accounts(self):
        return self.__account.all()

    def block_number(self):
        return self.__block.number()

    def get_balance(self, address, number):
        return self.__balance.of(address=address, number=number)

    def get_storage_at(self, address, position, number):
        return self.__storage.at(address=address, position=position, block_number=number)

    def get_transaction_count(self, address, number):
        return self.__transaction.count(address=address, number=number)

    def get_block_transaction_count_by_hash(self, hash):
        return self.__block_transaction_count.byHash(hash=hash)

    def get_block_transaction_count_by_number(self, number):
        return self.__block_transaction_count.byNumber(number=number)

    def get_uncle_count_by_block_hash(self, hash):
        return self.__uncle.countByBlockHash(hash=hash)

    def get_uncle_count_by_block_number(self, number):
        return self.__uncle.countByBlockNumber(number=number)

    def get_code(self, address, number):
        return self.__code.byAddressAndBlockNumber(address=address, number=number)

    def sign(self, address, message):
        return self.__sign.byAddress(address, message)

    def send_transaction(self, transaction: TransactionDTO):
        return self.__transaction.send(transaction=transaction)

    def send_raw_transaction(self, data):
        return self.__transaction.send_raw(data=data)

    def call(self, call_dto: CallDTO, number):
        return self.__transaction.call(dto=call_dto, number=number)

    def estimate_gas(self, transaction:TransactionDTO):
        return self.__transaction.estimate(transaction=transaction)

    def get_block_by_hash(self, hash, full=False):
        return self.__block.by_hash(hash=hash, full=full)

    def get_block_by_number(self, number, full=False):
        return self.__block.by_number(number=number, full=full)

    def get_transaction_by_hash(self, hash):
        return self.__transaction.by_hash(hash=hash)

    def get_transaction_by_block_hash_and_index(self, hash, index):
        return self.__transaction.by_blockhash_and_index(blockhash=hash, index=index)

    def get_transaction_by_block_number_and_index(self, number, index):
        return self.__transaction.by_blocknumber_and_index(blocknumber=number, index=index)

    def get_transaction_receipt(self, hash):
        return self.__transaction.receipt(hash=hash)

    def pending_transactions(self):
        return self.__transaction.pending()

    def get_uncle_by_block_hash_and_index(self, hash, index):
        return self.__uncle.byBlockHashAndIndex(hash=hash, index=index)

    def get_uncle_by_block_number_and_index(self, number, index):
        return self.__uncle.byBlockNumberAndIndex(number=number, index=index)

    def new_filter(self, filter_dto: FilterDTO):
        return self.__filter.create(filter_dto=filter_dto)

    def new_block_filter(self):
        return self.__filter.block_create()

    def new_pending_transaction_filter(self):
        return self.__filter.pending_transaction_create()

    def uninstall_filter(self, filter_id):
        return self.__filter.uninstall(filter_id=filter_id)

    def get_filter_changes(self, filter_id):
        return self.__logs.filter_changes(filter_id)

    def get_logs_filter_logs(self,filter_id):
        return self.__logs.filter_id(filter_id=filter_id)

    def get_logs(self, log_filter:LogFilterDTO):
        return self.__logs.filter(filter=log_filter)



