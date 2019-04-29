from pathlib import Path
from os.path import sep
import os
import json


class HelperFunctionCall:

    def __init__(self, name, inputs):
        self.name = name
        self.inputs = inputs
        self.call_string=""

    def get_call_string(self):
        args = ",".join(list(map(lambda f : f['type'], self.inputs)))
        return self.name+"("+args+")"


class HelperCallerWriter:

    @staticmethod
    def writer_method(helper_functions_array, name):
        template = get_template()
        template = template.replace("<Name>", name)

        enums = ""
        for h in helper_functions_array:
            enums += ("\n\t"+h.name.upper()+"=\""+h.get_call_string()+"\"")

        template = template.replace("<items>", enums)

        write_enum(name, template)

def write_enum(name, content):
    path_aux = "helper/generated/"+name+".py".replace("/", sep)
    path = os.path.join(Path(__file__).parent.parent, path_aux)

    with open(path, "w+") as fp:
        fp.write(content)
    fp.close()




def get_template():
    path_aux = "helper/temp".replace("/", sep)
    path = os.path.join(Path(__file__).parent.parent, path_aux)

    template = ""

    with open(path, 'r') as fp:
        line = fp.readline()
        while line:
            template += line
            line = fp.readline()

    return template

def get_abi():
    path_aux = "assets/abis/abi.json".replace("/", sep)
    path = os.path.join(Path(__file__).parent.parent, path_aux)
    file = open(path, 'r')
    return json.load(file)


def get_functions_name():
    functions_aux = get_abi()
    function = []
    for f in functions_aux:
        if f['type'] != "function":
            continue
        function.append(HelperFunctionCall(f['name'],f['inputs']))
    return function



HelperCallerWriter.writer_method(get_functions_name(), "DemoEnum")




