from src.modules.eth.ethereum import Ethereum
from src.modules.ipfs.ipfs import IPFS
from src.core.in3_core import In3Core


class In3Client:

    def __init__(self):
        self.wasm = None
        self.shh = None
        self.in3_core = In3Core()

        self.eth = Ethereum(self.in3_core)
        self.ipfs = IPFS()




