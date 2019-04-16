import rpc.eth.block.Block as bl
from  rpc.eth.block_transaction_count.block_transaction_count import BlockTransactionCount
from  rpc.eth.transaction.transaction import Transaction
from  rpc.eth.uncle.uncle import Uncle
from  rpc.eth.code.code import Code
from  rpc.eth.sign.sign import Sign
from  rpc.eth.account.account import Account
from  rpc.eth.balance.balance import Balance
from  rpc.eth.storage.storage import Storage
from  rpc.eth.gas.gas import Gas
from  rpc.eth.filter.filter import Filter
from  rpc.eth.logs.logs import Logs



from  utils.Utils import Config
from rpc.eth.enums.enums_execution_type import EnumsExecutionType


class Ethereum(object):

    def __init__(self, execution_type=EnumsExecutionType.NORMAL):
        Config.execution_type = execution_type
        self.block = bl.Block(execution_type)
        self.block_transaction_count = BlockTransactionCount(execution_type)
        self.transaction = Transaction(execution_type)
        self.uncle = Uncle(execution_type)
        self.code = Code(execution_type)
        self.sign = Sign(execution_type)
        self.account = Account(execution_type)
        self.balance = Balance(execution_type)
        self.storage = Storage(execution_type)
        self.gas = Gas(execution_type)
        self.filter= Filter(execution_type)
        self.logs = Logs(execution_type)


