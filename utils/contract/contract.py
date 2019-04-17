from utils.Utils import Hex
from utils.Utils import Hash
import re

class ContractUtils:

    def get_method_signature(self, method_signature):
        aux = self.change_signature(method_signature)
        return Hash.keccak(aux, 4)

    def getHexValue(self, item):
        complex_return = []
        if isinstance(item, str):
            return Hex.from_string_to_hex(item, 32)
        if isinstance(item, list):
            for i in item:
                complex_return.append(self.getHexValue(i))
            return "".join(complex_return)

        return Hex.from_int_to_hex(item, 32)


    def signature_hash_call(self, string_method_signature, params, prefix=""):

        result = self.get_method_signature(string_method_signature)

        for p in params:
            result+=self.getHexValue(p)

        prefix+=result
        return prefix

    def signature_hash_call_with_dynamic_types(self, string_method_signature, params, prefix=""):
        result = self.get_method_signature(string_method_signature)
        items = self.pre_compile_signature(string_method_signature)

        print(items)

        i=0
        dynamic_index = len(items)
        sub_result = ""
        for p in params:
            # result += self.getHexValue(p)
            aux = self.getHexValue(p)
            # print(items[i].is_dynamic,p, aux)
            if items[i].is_dynamic:
                index=dynamic_index*32
                result += self.getHexValue(index)

                if isinstance(p,list):
                    dynamic_index+=(len(p)+1)
                else:
                    dynamic_index+=2

                sub_result+= self.getHexValue(len(p))
                sub_result+= self.getHexValue(p)
            else:
                result += self.getHexValue(p)


            i+=1

        result+=sub_result

        prefix += result
        return prefix

    def change_signature(self, signature):
        result = re.sub(" ","",signature)
        result = re.sub("uint\[\]","uint256[]",result)
        result = re.sub("uint\,","uint256,",result)
        result = re.sub("uint\)","uint256)",result)
        return result

    def is_item_dynamic(self, item=""):
        is_dynamic =  item.endswith("[]")
        if(is_dynamic):
            return is_dynamic

        item = re.sub("[^0-9a-zA-Z]*", "", item)
        return item.find("bytes")>-1 and len(item)==len("bytes")


    def pre_compile_signature(self, signature):
        result_index = []
        new_signature = self.change_signature(signature)

        aux_signature_group = re.search("\((.*?)\)", new_signature)
        if aux_signature_group is None:
            print("erro")

        splited_arr = aux_signature_group.group().split(",")
        i=0
        for s in splited_arr:
            # print(s, self.is_item_dynamic(s))
            result_index.append(ItemSignatureIndex( i , self.is_item_dynamic(s)))
            i+=1



        return result_index



class ItemSignatureIndex:

    def __init__(self, index, is_dynamic):
        self.index = index
        self.is_dynamic = is_dynamic

