from enum import Enum,unique
from src.domain.chain import Chain

@unique
class EnumsChains(Enum):

    MAINNET = Chain(registry="0x2736D225f85740f42D17987100dc8d58e9e16252",
                    chain_id="0x1",
                    alias="mainnet",
                    status="https://in3.slock.it?n=mainnet",
                    node_list="https://in3.slock.it/mainnet/nd-3")

    KOVAN = Chain(
                    registry= "0x27a37a1210df14f7e058393d026e2fb53b7cf8c1",
                    chain_id= "0x2a",
                    alias="kovan",
                    status= "https://in3.slock.it?n=kovan",
                    node_list= "https://in3.slock.it/kovan/nd-3")

    TOBALABA = Chain(
                    registry="0x845E484b505443814B992Bf0319A5e8F5e407879",
                    chain_id="0x44d",
                    alias="tobalaba",
                    status="https://in3.slock.it?n=tobalaba",
                    node_list="https://in3.slock.it/tobalaba/nd-3")

    EVAN = Chain(
                    registry="0x85613723dB1Bc29f332A37EeF10b61F8a4225c7e",
                    chain_id="0x4b1",
                    alias="evan",
                    status="https://in3.slock.it?n=evan",
                    node_list="https://in3.slock.it/evan/nd-3")

    GOERLI = Chain(
                    registry="0x85613723dB1Bc29f332A37EeF10b61F8a4225c7e",
                    chain_id="0x5",
                    alias="goerli",
                    status="https://in3.slock.it?n=goerli",
                    node_list="https://in3.slock.it/goerli/nd-3")

    IPFS = Chain(
                    registry="0xf0fb87f4757c77ea3416afe87f36acaa0496c7e9",
                    chain_id="0x7d0",
                    alias="ipfs",
                    status="https://in3.slock.it?n=ipfs",
                    node_list="https://in3.slock.it/ipfs/nd-3")




