from enum import Enum, unique


@unique
class EnumsEthCall(Enum):

    RPC_ACCOUNT_ALL="eth_accounts"

    RPC_BALANCE_OF="eth_getBalance"

    RPC_STORAGE_AT="eth_getStorageAt"

    RPC_GAS_PRICE="eth_gasPrice"

    RPC_BLOCK_NUMBER = "eth_blockNumber"
    RPC_BLOCK_BY_NUMBER="eth_getBlockByNumber"
    RPC_BLOCK_BY_HASH="eth_getBlockByHash"

    RPC_BLOCK_TRANSACTION_COUNT_BY_NUMBER = "eth_getBlockTransactionCountByNumber"
    RPC_BLOCK_TRANSACTION_COUNT_BY_HASH = "eth_getBlockTransactionCountByHash"

    RPC_TRANSACTION_BY_HASH="eth_getTransactionByHash"
    RPC_TRANSACTION_BY_BLOCKHASH_AND_INDEX="eth_getTransactionByBlockHashAndIndex"
    RPC_TRANSACTION_BY_BLOCKNUMBER_AND_INDEX="eth_getTransactionByBlockNumberAndIndex"
    RPC_TRANSACTION_RECEIPT_BY_HASH="eth_getTransactionReceipt"
    RPC_TRANSACTION_PENDING="eth_pendingTransactions"
    RPC_TRANSACTION_COUNT = "eth_getTransactionCount"
    RPC_TRANSACTION_SEND = "eth_sendTransaction"
    RPC_TRANSACTION_SEND_RAW = "eth_sendRawTransaction"
    RPC_TRANSACTION_CALL = "eth_call"
    RPC_TRANSACTION_ESTIMATE="eth_estimateGas"

    RPC_UNCLE_COUNT_BY_BLOCK_HASH = "eth_getUncleCountByBlockHash"
    RPC_UNCLE_COUNT_BY_BLOCK_NUMBER = "eth_getUncleCountByBlockNumber"
    RPC_UNCLE_BY_BLOCKHASH_AND_INDEX="eth_getUncleByBlockHashAndIndex"
    RPC_UNCLE_BY_BLOCKNUMBER_AND_INDEX="eth_getUncleByBlockNumberAndIndex"

    RPC_CODE_BY_ADDRESS_AND_NUMBER="eth_getCode"

    RPC_SIGN_BY_ADDRESS="eth_sign"

    RPC_FILTER_NEW="eth_newFilter"
    RPC_FILTER_NEW_BLOCK="eth_newBlockFilter"
    RPC_FILTER_NEW_PENDING_TRANSACTION="eth_newPendingTransactionFilter"
    RPC_FILTER_UNINSTALL="eth_uninstallFilter"

    RPC_LOGS_FILTER_CHANGES="eth_getFilterChanges"
    RPC_LOGS_FILTER_ID="eth_getFilterLogs"
    RPC_LOGS_FILTER="eth_getLogs"





