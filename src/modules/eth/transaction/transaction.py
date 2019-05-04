from src.utils.Utils import Mockable
from src.core.rpc_direct_core import RPCDirectCore
from src.utils.Utils import Config

from src.enums.enums_eth_call import EnumsEthCall
from src.enums.enums_execution_type import EnumsExecutionType
from src.enums.enums_block_status import EnumsBlockStatus

from src.dto.transaction_dto import TransactionDTO
from src.dto.call_dto import CallDTO


class Transaction:

    def __init__(self, execution_type=EnumsExecutionType.NORMAL):
        self.execution_type = execution_type

    @Mockable("transaction.byHash")
    def by_hash(self, hash):
        return TransactionService().call_transaction_by_hash(hash)

    @Mockable("transaction.byBlockHashAndIndex")
    def by_blockhash_and_index(self, blockhash, index="0x0"):
        return TransactionService().call_transaction_by_blockhash_and_index(blockhash, index)

    @Mockable("transaction.byBlockNumberAndIndex")
    def by_blocknumber_and_index(self, blocknumber, index="0x0"):
        if isinstance(blocknumber, EnumsBlockStatus):
            blocknumber = blocknumber.value

        return TransactionService().call_transaction_by_blocknumber_and_index(blocknumber, index)

    @Mockable("transaction.receiptByHash")
    def receipt(self, hash):
        return TransactionService().call_receipt_by_transaction_hash(hash)

    @Mockable("transaction.pending")
    def pending(self):
        return TransactionService().call_transaction_pending()

    @Mockable("transaction.count")
    def count(self, address, number):
        if isinstance(number, EnumsBlockStatus):
            number = number.value
        return TransactionService().call_transaction_count(address, number)

    @Mockable("transaction.send")
    def send(self, transaction: TransactionDTO):
        return TransactionService().call_transaction_send(transaction)

    @Mockable("transaction.send")
    def send_raw(self, data):
        return TransactionService().call_raw_transaction_send(data)


    @Mockable("transaction.call")
    def call(self, dto:CallDTO, number):
        if isinstance(number, EnumsBlockStatus):
            number = number.value
        return TransactionService().call_message(dto,number)

    @Mockable("transaction.estimate")
    def estimate(self, transaction: TransactionDTO):
        return TransactionService().call_estimate_gas(transaction)


class TransactionService(object):

    def call_transaction_by_hash(self,hash):
        params = []
        params.append(hash)

        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_TRANSACTION_BY_HASH, params=params)

    def call_transaction_by_blockhash_and_index(self, blockhash,index):
        params = []
        params.append(blockhash)
        params.append(index)

        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_TRANSACTION_BY_BLOCKHASH_AND_INDEX, params=params)


    def call_transaction_by_blocknumber_and_index(self, blocknumber,index):
        params = []
        params.append(blocknumber)
        params.append(index)

        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_TRANSACTION_BY_BLOCKNUMBER_AND_INDEX, params=params)


    def call_receipt_by_transaction_hash(self,hash):
        params = []
        params.append(hash)

        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_TRANSACTION_RECEIPT_BY_HASH, params=params)

    def call_transaction_pending(self):
        params = []

        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_TRANSACTION_PENDING, params=params)

    def call_transaction_count(self, address, number):
        params=[]
        params.append(address)
        params.append(number)
        if Config.execution_type== EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_TRANSACTION_COUNT, params=params)

    def call_transaction_send(self, transactionDTO:TransactionDTO):
        params = []
        params.append(transactionDTO.toJson())
        if Config.execution_type== EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_TRANSACTION_SEND, params=params)

    def call_raw_transaction_send(self, data):
        params = []
        params.append(data)
        if Config.execution_type== EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_TRANSACTION_SEND_RAW, params=params)


    def call_message(self, dto:CallDTO, number):
        params = []
        params.append(dto.toJson())
        params.append(number)

        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_TRANSACTION_CALL, params=params)

    def call_estimate_gas(self, dto: TransactionDTO):
        params = []
        params.append(dto.toJson())
        if Config.execution_type == EnumsExecutionType.RPC_DIRECT:
            return RPCDirectCore().rpc_call(enums_eth_call=EnumsEthCall.RPC_TRANSACTION_ESTIMATE, params=params)
