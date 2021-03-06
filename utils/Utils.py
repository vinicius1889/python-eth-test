from pathlib import Path
from os.path import sep
import os
import requests
import json
from  rpc.eth.enums.enums_execution_type import EnumsExecutionType
from Crypto.Hash import  keccak



def get_mock(item):
    path_aux = "assets/mocks/rpc/eth/mock.json".replace("/", sep)
    path = os.path.join(Path(__file__).parent.parent, path_aux)
    file = open(path, 'r')
    my_json = json.load(file)
    file.close()
    arr = item.split(".")
    item = None
    for a in arr:
        if item is None:
            item = my_json[a]
        else:
            item = item[a]

    return item


class Mockable(object):

    def __init__(self, arg1):
        self.arg1 = arg1

    def __call__(self, func, *args, **kwargs):
        def inner_func(*args, **kwargs):
            if Config.execution_type == EnumsExecutionType.MOCK:
                return get_mock(self.arg1)
            return func(*args, **kwargs)
        return inner_func


class Config:

    execution_type = EnumsExecutionType.NORMAL


class RPC:


    def call(self, method, params=[], url="http://rpc.slock.it/tobalaba", id=1, headers={'content-type':'application/json'}):
        body = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": id
        }
        return requests.post(url, data=json.dumps(body), headers=headers).json()

class Hex:



    @staticmethod
    def to_string(param:str):
        if param.startswith("0x"):
            param = param[len("0x"):]
        return bytearray.fromhex(param).decode()

    @staticmethod
    def to_int(param):
        return int(param, 16)


    @staticmethod
    def from_string_to_hex(param:str, pad_to_bytes=0):
        hash =  param.encode("utf-8").hex()
        if pad_to_bytes>0:
            return hash.ljust(pad_to_bytes*2,'0')

        return hash


    @staticmethod
    def from_int_to_hex(param, pad_to_bytes=0):
        result = hex(param)
        if pad_to_bytes >0:
            aux = result[2:]
            return aux.zfill(pad_to_bytes*2)

        return result


class Hash:

    @staticmethod
    def keccak(string:str, length_in_bytes=0):
        kek = keccak.new(digest_bits=256)
        kek.update(string.encode("utf-8"))
        hash = kek.hexdigest()
        if length_in_bytes>0:
            return hash[:length_in_bytes*2]
        return hash



