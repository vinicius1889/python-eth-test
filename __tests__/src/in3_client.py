from unittest import TestCase
from src.in3_client import In3Client
from src.domain.in3_types import IN3Config
from src.enums.enums_chains import EnumsChains

class In3ClientTestCase(TestCase):

    @staticmethod
    def create_in3_client_instance():
        return In3Client()

    def test_new_incubed(self):
        self.assertIsNotNone(In3ClientTestCase.create_in3_client_instance())

    def test_new_ipfs_api(self):
        self.assertIsNotNone(In3ClientTestCase.create_in3_client_instance().ipfs)

    def test_build_config_from_json(self):
        in3 = In3Client.create_in3_client_from_default_config()
        self.assertIsNotNone(in3)

    def test_build_in3(self):
        config = IN3Config()
        config.chainId = EnumsChains.MAINNET.value.chain_id
        in3 = In3Client(config=config)



        self.assertIsNotNone(in3)
        self.assertIsNotNone(in3.eth)
        self.assertIsNotNone(in3.ipfs)

