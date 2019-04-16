# import libin3
from rpc.eth.enums.enums_eth_call import EnumsEthCall
from utils.Utils import RPC
from utils.Utils import Config
import json

class RPCDirectCore(object):

    def __init__(self):
        pass

    def rpc_call(self, enums_eth_call: EnumsEthCall, params=[]):
        print("\n********************** ")
        print("Direct RPC Call\n")
        print("Calling RPC ", enums_eth_call.value, "with parameters ", params, " execution type = ",Config.execution_type.value )
        result = RPC().call(enums_eth_call.value,params)

        print("\nJSON inline\n")
        print(result)
        print("\nJSON verbose\n")
        print(json.dumps(result, indent=4, sort_keys=True))

        return result



