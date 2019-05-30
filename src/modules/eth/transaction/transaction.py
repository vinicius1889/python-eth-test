from src.utils.Utils import Mockable
from src.core.rpc_direct_core import RPCDirectCore
from src.utils.Utils import Config

from src.enums.enums_eth_call import EnumsEthCall
from src.enums.enums_execution_type import EnumsExecutionType
from src.enums.enums_block_status import EnumsBlockStatus

from src.dto.transaction_dto import TransactionDTO
from src.dto.call_dto import CallDTO


from src.core.in3_core import In3Core


class Transaction:

    def __init__(self, in3_core:In3Core):
        self.in3_core = in3_core


    def by_hash(self, hash):
        params = []
        params.append(hash)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_TRANSACTION_BY_HASH, params)

    def by_blockhash_and_index(self, blockhash, index="0x0"):
        params = []
        params.append(blockhash)
        params.append(index)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_TRANSACTION_BY_BLOCKHASH_AND_INDEX, params)

    def by_blocknumber_and_index(self, blocknumber, index="0x0"):
        params = []
        params.append(blocknumber)
        params.append(index)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_TRANSACTION_BY_BLOCKNUMBER_AND_INDEX, params)

    def receipt(self, hash):
        params = []
        params.append(hash)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_TRANSACTION_RECEIPT_BY_HASH, params)

    def pending(self):
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_TRANSACTION_PENDING, [])

    def count(self, address, number):
        params = []
        params.append(address)
        params.append(number)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_TRANSACTION_COUNT, params)

    def send(self, transaction: TransactionDTO):
        params = []
        params.append(transaction.toJson())
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_TRANSACTION_SEND, params)

    def send_raw(self, data):
        params = []
        params.append(data)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_TRANSACTION_SEND_RAW, params)

    def call(self, dto:CallDTO, number):
        params = []
        params.append(dto.toJson())
        params.append(number)
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_TRANSACTION_CALL, params)

    def estimate(self, transaction: TransactionDTO):
        params = []
        params.append(transaction.toJson())
        return self.in3_core.in3_raw_rpc_wrapper(EnumsEthCall.RPC_TRANSACTION_ESTIMATE, params)

