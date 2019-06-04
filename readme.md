This is a simple test using in3 python library

### Creating a new instance 
```
in3 = In3Client()
```

### Creating a new instance from default configurations
```
In3Client.create_in3_client_from_default_config()
```

### Creating a new instance from my custom configuration
```
config = IN3Config()
config.chainId = EnumsChains.MAINNET.value.chain_id
in3 = In3Client(config=config)
```

### Calling ETH function from our In3 Client

```
in3  = In3Client.create_in3_client_from_default_config()
in3.eth.block_number()
```


## Functions

We can call different kinds of functions using the In3 Client.

##### *IPFS will be supported soon


### Ethereum

You can call ethereum functions using our client

* Assuming that you have the In3 Client setted correctly as we did before, we can call these functions.


```
in3 = In3Client.create_in3_client_from_default_config()
in3.eth
```


The eth module is responsible to call all ethereum functions using our client to make the things easier.


#### [gas_price](https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_gasprice)

Returns the current price per gas in wei.


```python
in3.eth.gas_price()

```


#### [accounts](https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_accounts)

Return all accounts

```python
in3.eth.accounts()

```


#### [eth_blockNumber](https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_blockNumber)

Returns the number of most recent block.


```python
in3.eth.block_number()

```


#### [eth_getBalance](https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getBalance)

Returns the balance of the account of given address.

```python
address = '0xc94770007dda54cF92009BFF0dE90c06F603a09f'
in3.eth.get_balance(address, EnumsBlockStatus.LATEST)
```

