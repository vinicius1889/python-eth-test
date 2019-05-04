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


##### *IPFS will be supported soon



