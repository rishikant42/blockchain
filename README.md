# Blockchain
---
Wiki: A blockchain is a continuously growing list of records, called blocks, which are linked and secured using cryptography

Note: It is NOT secure neither a real blockchain and you should NOT use this for anything else than educational purposes.

### Features:
```
==> Blockchain Client

* Wallet generation using public key cryptography

* Can create a new transaction & submit it to network

==> Blockchain Network

* Transactions with RSA encryption

* Coin mining

* Proof of work(Hash algo: sha256)

* Coin incentive

* Node resolve conflict

```
### Install:
```
pip install blockchainpy
```

### Examples:

## Create wallet

==> It's a key-pair of `privat_key` & `address`. Address is public address to recieve coin. Private-key is use to send coins to some address.

```
In [1]: from blockchain.client import create_wallet

In [2]: alice_wallet = create_wallet()

In [3]: bob_wallet = create_wallet()

In [4]: print alice_wallet
{'private_key': u'3082025b02010002818100a14e2c39b663192c1f191b97e0448da2e4a49599f318903af71e2c5b0061b68555fa86a37661fa66e391ba226f1b91b64cad657af93adbdd0b011150d6796b8512497ab79f92513d24c199008136b8d9ae8430559fead5ee00ba70afa4c5c4de56cdba1ef22c84f327be218047e7f9355c7d4a13bfa248703a141000b2f35409020301000102818059f5c50872c595d65b899f2ff6ad84e861e7c05f598a4b75f737e6b8e1df9cf183dff292db850d27b0a7274de8f551308056fc0fb74bb22ef6e2238c17f1239af2ca25a20dc7b78de01df3681dcf452b8b3e549c0bb4079b510cf7d7df4c9ae18f3d96b786e3b194c3c95e53dd4aaf95b4540c1dd2d4e9367ab6836890aaf201024100c9906133f3a7c42326f742469fb29ebf358c0e3a2049f517f519db7063dd9a3d0183e42974c242d0c73992d10fa9ee6c2846f03d4f6d0a6548f82e66867d3629024100ccde6a2152f3a216b3a56a9e062a714c7e31f9620716578840d415bd0da22e2526486840bb12165e9320e6f49e786c159034b90d665e7b71eaac14b5ec642ae10240212de7124a357f8fd9c631deb6430ce6a4c5dd41ac370065652f5073fbbc6abb481891e25119f92dacddc95128a6ec5c5974f3eee3b82b51e8e5119e46dd2da102407ef59ec3c40a63fab99ddb72ced3629f4add6174d47b8e074c55a29b2465cb3f0e7874d3189b5eed813434ac87c08d0ad7f134750f69a20ab8a9a7b40e290d4102402a9aeaeb5d1a10c191dac5ccf12a91f1dfa8db5b01adf110f52fc35991c569cb42d6bab579b8a15b99da88fdfb0f1c78b581834535e94541b02260ea697eab0e', 'address': u'30819f300d06092a864886f70d010101050003818d0030818902818100a14e2c39b663192c1f191b97e0448da2e4a49599f318903af71e2c5b0061b68555fa86a37661fa66e391ba226f1b91b64cad657af93adbdd0b011150d6796b8512497ab79f92513d24c199008136b8d9ae8430559fead5ee00ba70afa4c5c4de56cdba1ef22c84f327be218047e7f9355c7d4a13bfa248703a141000b2f354090203010001'}

```

## Check balance

==> Amount of coins that particular address have.

```
In [5]: from blockchain.network import check_balance

In [6]: print check_balance(alice_wallet['address'])
None

In [7]: print check_balance(bob_wallet['address'])
None

```

## Genesis block/transaction
==> A genesis block is the first block of a block chain. The genesis block is almost always hardcoded into the software of the applications that utilize its block chain. It is a special case in that it does not reference a previous block.
==> In our case, Genesis transaction will send 50 coin to given address.

```
In [9]: create_genesis_transaction(alice_wallet['address'])
Out[9]: 
{'block_number': 1,
 'nonce': "I'm special. I didn't go through mining process",
 'previous_hash': '00000',
 'timestamp': 1529315091.63091,
 'transactions': [OrderedDict([('sender_address', 'Author'),
               ('recipient_address',
                u'30819f300d06092a864886f70d010101050003818d0030818902818100a14e2c39b663192c1f191b97e0448da2e4a49599f318903af71e2c5b0061b68555fa86a37661fa66e391ba226f1b91b64cad657af93adbdd0b011150d6796b8512497ab79f92513d24c199008136b8d9ae8430559fead5ee00ba70afa4c5c4de56cdba1ef22c84f327be218047e7f9355c7d4a13bfa248703a141000b2f354090203010001'),
               ('value', 50)])]}

In [10]: print check_balance(alice_wallet['address'])
50
```

## Create new transaction
==> One can create a transaction using blockchain client and submit it blockchain network. Miner will pick the transaction and add to blockchain if it is valid.
==> Send 10 coin from Alice-wallet to Bob-wallet

```
In [11]: from blockchain.client import

In [12]: txn=create_transaction(alice_wallet['address'], alice_wallet['private_key'], bob_wallet['address'], 10)
    ...:
    ...: sign = txn.get('signature')
    ...:
    ...: sender = txn.get('transaction').get('sender_address')
    ...:
    ...: reciver = txn.get('transaction').get('recipient_address')
    ...:
    ...: value = txn.get('transaction').get('value')
    ...:

In [13]: print txn
{'transaction': OrderedDict([('sender_address',
u'30819f300d06092a864886f70d010101050003818d0030818902818100a14e2c39b663192c1f191b97e0448da2e4a49599f318903af71e2c5b0061b68555fa86a37661fa66e391ba226f1b91b64cad657af93adbdd0b011150d6796b8512497ab79f92513d24c199008136b8d9ae8430559fead5ee00ba70afa4c5c4de56cdba1ef22c84f327be218047e7f9355c7d4a13bfa248703a141000b2f354090203010001'),
('recipient_address',
u'30819f300d06092a864886f70d010101050003818d0030818902818100bed5a04c1ab5855f2329527d674a07a4ecd07ffbb1e662f319fb8eea04794eb4991340d1bae42c7adf75405007c355573b7629a16d211e39ba1d63cf8f17655ab92c95eb95d15b2e6730266e79c1b4e2e3a39978237ca09b7e35e87e41ae610f3442a557a91b85679534fe6cf768db4cee34324a3edf768801fe2411b01fee470203010001'),
('value', 10)]), 'signature':
u'78eba5404647d3e6ed9d34c6040226ab2924b03dcc2ee7706c5030d85b0cc7984cfa1572d63b461d8e2ad74b896d7966788a5ecda092428b3559655ee157bbef0361d4f69f9ff3748f8c9e455fa3dbf9a2e9916214d6485784e6c7a3b085ef36e674ec701763dfecf42795f590c28eb5e64cf1fca73bbba2c0f3cb5e6cb7aa77'}

```

## Mining
==> One of the miner will pick the transaction & add it block if it is valid. In our case, we will have to manually submit the transaction to the network
==> To mine a block, miners need to find an extremely rare solution to a cryptographic puzzle. If a mined block is accepted by the blockchain, the miner receive a reward in coins which is an additional incentive to transaction fees.
==> The mining process is also referred to as Proof of Work (PoW), and it's the main mechanism that enables the blockchain to be trustless and secure.

```
In [14]: from blockchain.network import new_transaction

In [15]: new_transaction(sender, reciver, value, sign)

In [15]: new_transaction(sender, reciver, value, sign)
Out[15]: {'message': 'Transaction will be added to Block 3'}

In [16]: from blockchain.network import mine

In [17]: mine()
Out[17]: 
{'block_number': 3,
 'message': 'New Block Forged',
 'nonce': 104,
 'previous_hash': 'feb69b361108c517144464d04a7dcb30a7f109ea48d74f0985f9efe97666bf9f',
 'transactions': [OrderedDict([('sender_address',
                u'30819f300d06092a864886f70d010101050003818d0030818902818100a14e2c39b663192c1f191b97e0448da2e4a49599f318903af71e2c5b0061b68555fa86a37661fa66e391ba226f1b91b64cad657af93adbdd0b011150d6796b8512497ab79f92513d24c199008136b8d9ae8430559fead5ee00ba70afa4c5c4de56cdba1ef22c84f327be218047e7f9355c7d4a13bfa248703a141000b2f354090203010001'),
               ('recipient_address',
                u'30819f300d06092a864886f70d010101050003818d0030818902818100bed5a04c1ab5855f2329527d674a07a4ecd07ffbb1e662f319fb8eea04794eb4991340d1bae42c7adf75405007c355573b7629a16d211e39ba1d63cf8f17655ab92c95eb95d15b2e6730266e79c1b4e2e3a39978237ca09b7e35e87e41ae610f3442a557a91b85679534fe6cf768db4cee34324a3edf768801fe2411b01fee470203010001'),
               ('value', 10)]),
  OrderedDict([('sender_address', 'THE BLOCKCHAIN'),
               ('recipient_address', '98ed1fd7b9c64327ba8bcc2f76631ddd'),
               ('value', 1)])]}
```

## Full chain

==> Since blockchain is public ledger, one can check complete blockchain & can verify his/her transaction in chain
```
In [18]: from blockchain.network import full_chain                                                       [23/572]
                                                                                                                 
In [19]: full_chain()                                                                                            
Out[19]:                                                                                                         
{'chain': [{'block_number': 1,                                                                                   
   'nonce': 0,                                                                                                   
   'previous_hash': '00',                                                                                        
   'timestamp': 1529314632.98755,                                                                                
   'transactions': []},                                                                                          
  {'block_number': 1,                                                                                            
   'nonce': "I'm special. I didn't go through mining process",                                                   
   'previous_hash': '00000',                                                                                     
   'timestamp': 1529315091.63091,                                                                                
   'transactions': [OrderedDict([('sender_address', 'Author'),                                                   
                 ('recipient_address',                                                                           
                  u'30819f300d06092a864886f70d010101050003818d0030818902818100a14e2c39b663192c1f191b97e0448da2e4a
49599f318903af71e2c5b0061b68555fa86a37661fa66e391ba226f1b91b64cad657af93adbdd0b011150d6796b8512497ab79f92513d24c1
99008136b8d9ae8430559fead5ee00ba70afa4c5c4de56cdba1ef22c84f327be218047e7f9355c7d4a13bfa248703a141000b2f3540902030
10001'),                                                                                                         
                 ('value', 50)])]},   
  {'block_number': 3,
   'nonce': 104,
   'previous_hash': 'feb69b361108c517144464d04a7dcb30a7f109ea48d74f0985f9efe97666bf9f',
   'timestamp': 1529316112.395494,
   'transactions': [OrderedDict([('sender_address',
                  u'30819f300d06092a864886f70d010101050003818d0030818902818100a14e2c39b663192c1f191b97e0448da2e4a
49599f318903af71e2c5b0061b68555fa86a37661fa66e391ba226f1b91b64cad657af93adbdd0b011150d6796b8512497ab79f92513d24c199008136b8d9ae8430559fead5ee00ba70afa4c5c4de56cdba1ef22c84f327be218047e7f9355c7d4a13bfa248703a141000b2f354090203010001'),
                 ('recipient_address',
                  u'30819f300d06092a864886f70d010101050003818d0030818902818100bed5a04c1ab5855f2329527d674a07a4ecd
07ffbb1e662f319fb8eea04794eb4991340d1bae42c7adf75405007c355573b7629a16d211e39ba1d63cf8f17655ab92c95eb95d15b2e6730
266e79c1b4e2e3a39978237ca09b7e35e87e41ae610f3442a557a91b85679534fe6cf768db4cee34324a3edf768801fe2411b01fee4702030
10001'),
                 ('value', 10)]),
    OrderedDict([('sender_address', 'THE BLOCKCHAIN'),
                 ('recipient_address', '98ed1fd7b9c64327ba8bcc2f76631ddd'),
                 ('value', 1)])]}],
 'length': 3}
```

## Updated wallet balaces
```
In [20]: print check_balance(alice_wallet['address'])
40

In [21]: print check_balance(bob_wallet['address'])
10
```

### ToDo:
```
* Balance verification should be done in mining step. Right now, it's in new-transaction method
* Balance should get update after mining step.
```

### License

See the [LICENSE](LICENSE) file for license rights and limitations (MIT).
