#!/usr/bin/env bash


curl -X POST --data '{"method":"eth_getBlockTransactionCountByNumber","jsonrpc":"2.0","id":1,"params":["0xe8"]}' -H "Content-Type: application/json"  https://in3.slock.it/mainnet/nd-3

