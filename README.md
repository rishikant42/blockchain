#Blockchain
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

## create wallet

==> It's a key-pair of `privat_key` & `address`. Address is public address to recieve coin. Private-key is use to send coins to some address.

```
In [1]: from blockchain.client import create_wallet

In [2]: alice_wallet = create_wallet()

In [3]: bob_wallet = create_wallet()

In [4]: print alice_wallet
{'private_key': u'3082025b02010002818100a14e2c39b663192c1f191b97e0448da2e4a49599f318903af71e2c5b0061b68555fa86a37661fa66e391ba226f1b91b64cad657af93adbdd0b011150d6796b8512497ab79f92513d24c199008136b8d9ae8430559fead5ee00ba70afa4c5c4de56cdba1ef22c84f327be218047e7f9355c7d4a13bfa248703a141000b2f35409020301000102818059f5c50872c595d65b899f2ff6ad84e861e7c05f598a4b75f737e6b8e1df9cf183dff292db850d27b0a7274de8f551308056fc0fb74bb22ef6e2238c17f1239af2ca25a20dc7b78de01df3681dcf452b8b3e549c0bb4079b510cf7d7df4c9ae18f3d96b786e3b194c3c95e53dd4aaf95b4540c1dd2d4e9367ab6836890aaf201024100c9906133f3a7c42326f742469fb29ebf358c0e3a2049f517f519db7063dd9a3d0183e42974c242d0c73992d10fa9ee6c2846f03d4f6d0a6548f82e66867d3629024100ccde6a2152f3a216b3a56a9e062a714c7e31f9620716578840d415bd0da22e2526486840bb12165e9320e6f49e786c159034b90d665e7b71eaac14b5ec642ae10240212de7124a357f8fd9c631deb6430ce6a4c5dd41ac370065652f5073fbbc6abb481891e25119f92dacddc95128a6ec5c5974f3eee3b82b51e8e5119e46dd2da102407ef59ec3c40a63fab99ddb72ced3629f4add6174d47b8e074c55a29b2465cb3f0e7874d3189b5eed813434ac87c08d0ad7f134750f69a20ab8a9a7b40e290d4102402a9aeaeb5d1a10c191dac5ccf12a91f1dfa8db5b01adf110f52fc35991c569cb42d6bab579b8a15b99da88fdfb0f1c78b581834535e94541b02260ea697eab0e', 'address': u'30819f300d06092a864886f70d010101050003818d0030818902818100a14e2c39b663192c1f191b97e0448da2e4a49599f318903af71e2c5b0061b68555fa86a37661fa66e391ba226f1b91b64cad657af93adbdd0b011150d6796b8512497ab79f92513d24c199008136b8d9ae8430559fead5ee00ba70afa4c5c4de56cdba1ef22c84f327be218047e7f9355c7d4a13bfa248703a141000b2f354090203010001'}

```

## check-Balance

==> Amount of coins that particular address have.

```
In [5]: from blockchain.network import check_balance

In [6]: print check_balance(alice_wallet['address'])
None

In [7]: print check_balance(bob_wallet['address'])
None

```


### License

See the [LICENSE](LICENSE) file for license rights and limitations (MIT).
