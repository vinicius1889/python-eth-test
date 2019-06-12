from typing import List, Mapping
from src.utils.Utils import JSONConfig
import json

class IN3NodeWeight:


    def __init__(self):
        self.weight:int=None
        self.responseCount:int=None
        self.avgResponseTime:int=None
        self.pricePerRequest:int=None
        self.lastRequest:int=None
        self.blacklistedUntil:int=None


class IN3NodeConfig:


    def __init__(self):
        self.index:int=None
        self.address:str=None
        self.timeout:int=None
        self.url:str=None
        self.chainIds:List[str]=None
        self.deposit:int=None
        self.capacity:int=None
        self.props:int=None


class ChainSpec:


    def __init__(self):
        self.engine:str=None
        self.validatorContract:str=None
        self.validatorList:List=None


class IN3ConfigServer:

    def __init__(self):
        self.verifier:str = None
        self.name:str = None
        self.chainSpec:ChainSpec = None



class IN3Config:


    def __init__(self):
        self.cacheTimeout=None
        self.nodeLimit:int=None
        self.keepIn3:bool=False
        self.format:str='json'
        self.key=None
        self.autoConfig:bool=None
        self.retryWithoutProof:bool=False
        self.maxAttempts:int=10
        self.includeCode:bool=False
        self.maxCodeCache:int=100000
        self.maxBlockCache:int=100
        self.verifiedHashes:str=None
        self.proof:str=None
        self.signatureCount:int=2
        self.minDeposit:int=None
        self.replaceLatestBlock:int=6
        self.requestCount:int=3
        self.finality:int=50
        self.timeout:int=3000
        self.chainId:str="0x1"
        self.chainRegistry:str=None
        self.mainChain:str=None
        self.autoUpdateList:bool=False
        self.cacheStorage=None
        self.loggerUrl:str=None
        self.servers:List[IN3ConfigServer]=None
        self.initAddresses:List[str]=None
        self.lastBlock:int=None
        self.contract:str=None
        self.needsUpdate:bool=False
        self.contractChain:str=None
        self.nodeList:List[IN3NodeConfig]=None
        self.nodeAuthorities:List[str]=None
        self.weights:Mapping[str, IN3NodeWeight]=None


    @staticmethod
    def build_from_default_config():
        in3_config = IN3Config()
        in3_config.__dict__.update(JSONConfig.get_in3_config())
        return in3_config



class In3Result:


    def __init__(self, request:str, success:bool, result:str,result_code:int):
        self.request = request
        self.success = success
        self.result = result
        self.result_code = result_code

    def get_json_request(self):
        return json.loads(self.request)

    def get_json_result(self):
        return json.loads(self.result)


class In3CallException(Exception):
    def __init__(self):
        super(In3CallException, self).__init__()
