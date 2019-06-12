from src.core.slib import libin3p as libin3
from src.enums.enums_eth_call import EnumsEthCall
from src.enums.enums_execution_type import EnumsExecutionType
from typing import List
from src.utils.Utils import params_to_json_string
from src.domain.in3_types import In3Result, In3CallException

from src.utils.Utils import Config

class In3Core(object):

    in3 = None

    @staticmethod
    def init_in3():
        if In3Core.in3 is None:
            aux = libin3.new_in3p()
            libin3.init_client(aux)
            In3Core.in3 = aux

    @staticmethod
    def close():
        libin3.delete_in3p(In3Core.in3)
        In3Core.in3 = None

    def __init__(self):
        In3Core.init_in3()

    def in3_raw_rpc(self, method: str, params:str):
        wrapper = libin3.new_WrapperCallp()

        if Config.debugging:
            print("**** Printing ****")
            print('method: {}'.format(method) )
            print('parameter: {}'.format(params))
            self.write_rpc_call_string_debug(method, params)
            wrapper.debug = True


        libin3.in3_client_rpc_raw(self.in3,method,params, wrapper)
        aux = self.get_result(wrapper)
        if not aux.success:
            error = "Error: method: {}, request: {}, result code: {}".format(aux.get_json_request()["method"], aux.request, aux.result_code)
            raise In3CallException(error)

        return aux.result

    def in3_raw_rpc_wrapper(self, method: EnumsEthCall, params:List):
        params_str = params_to_json_string(params)
        return self.in3_raw_rpc(method.value, params_str)

    def get_result(self, wrapper)->In3Result:
        aux = In3Result(request=wrapper.request,
                  success=wrapper.success,
                  result=wrapper.result,
                  result_code=wrapper.result_code)

        if Config.debugging:
            print(aux.__dict__)

        return aux

    def write_rpc_call_string_debug(self, method, params):
        rpc = "curl -X POST --data '{\"method\":\""+method+"\",\"jsonrpc\":\"2.0\",\"id\":1,\"params\":"+params+"}' -H 'Content-Type: application/json' <host>"
        print(rpc)



