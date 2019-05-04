from src.modules.eth.ethereum import Ethereum
from src.modules.ipfs.ipfs import IPFS
from src.domain.in3_types import IN3Config


class In3Client:

    def __init__(self, config: IN3Config= None):
        self.eth = Ethereum()
        self.ipfs = IPFS()
        self.__config: IN3Config = config
        self.wasm = None
        self.shh = None

    @staticmethod
    def create_in3_client_from_default_config():
        config = IN3Config.build_from_default_config()
        in3 = In3Client(config)
        return in3

    def get_config(self):
        return self.__config

