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

```
In [1]: from blockchain.client import make_wallet, make_transaction

In [2]: alice_wallet = make_wallet()

In [3]: print alice_wallet
{'private_key': u'3082025b02010002818100a3137c6536846d90ad3491019fd7cdc7c08cd9755b6d7e3eb633cd0becebcd826c74cdac10da76749509f805c8308e1857c8dfed211b07e0aa88821fd9898a3f5981b1c2cee4fa0c97be8c464d20f1e220336ec4411a87ef5a3923d15ca25586abe846e7bd8e392351c380e8b2caaf6864163bf7e5e0ae9b3997688f309a340d02030100010281807f5fb7f902451ba336766990a03e1a401c98a73db024ecc7a4deff18827c87ef88310f78874d6bda9192d0c40b62498a9ffe8951195b98a295f0bbda8eba8c5cc161052fe7e3b9745a8a1bb527391f020d8a973a3aad2c3e9c5a9492178fe7504e5eea2ed15077a339f5492c1b4edb5d966b82183d0ed750d08035caade851e1024100c3f436793b89a326f996a0574b8103ac8a684c4fd6095f836da23a8d8587d5aef8978f9849cdd96cdc33a229eddb0c30611bfb08e1df4add5516e9f34de040b5024100d50c2416cb587dfade0d6799503342d10e47fa41cc3ef2b89b8fa666fb6d248c02c19a401dcaa42dd11fc536766ca5645cbb3a3f9cb90c15ac1fec1f7d8cb4f90240204e8230a8ad3f95ec6e760f0e66bde953847098750c648ff1a25e8ef8a5f587fc7a58755e2daf1c308ddebd94f69962dc8fd56a987acd0802c05d5ffcc5ed4502403b9222813128b449324fc3390e40d71d07863ec6a92aacc9cbcd95f4d3b6c7f2524efa27956cf50d4e9d3892aaf86422b4ff31215a5c2fb1dba82d68fcbd1c59024061ea7f0763b53cf06f23e6c7f3835223b62afb63ae54440410c7f96b957cd85ef2652f9370db7738e8d8aa79b5e4afc42c9b1f0c8ca7124cecb7c9ec3914f9a1', 'address': u'30819f300d06092a864886f70d010101050003818d0030818902818100a3137c6536846d90ad3491019fd7cdc7c08cd9755b6d7e3eb633cd0becebcd826c74cdac10da76749509f805c8308e1857c8dfed211b07e0aa88821fd9898a3f5981b1c2cee4fa0c97be8c464d20f1e220336ec4411a87ef5a3923d15ca25586abe846e7bd8e392351c380e8b2caaf6864163bf7e5e0ae9b3997688f309a340d0203010001'}

In [4]: bob_wallet = make_wallet()

In [5]:
In [6]: create_genesis_transaction(alice_wallet['address'])
Out[6]: 
{'block_number': 1,
 'nonce': "I'm special. I didn't go through mining process",
 'previous_hash': '00000',
 'timestamp': 1529263303.059447,
 'transactions': [OrderedDict([('sender_address', 'Author'),
               ('recipient_address',
                u'30819f300d06092a864886f70d010101050003818d0030818902818100a3137c6536846d90ad3491019fd7cdc7c08cd9755b6d7e3eb633cd0becebcd826c74cdac10da76749509f805c8308e1857c8dfed211b07e0aa88821fd9898a3f5981b1c2cee4fa0c97be8c464d20f1e220336ec4411a87ef5a3923d15ca25586abe846e7bd8e392351c380e8b2caaf6864163bf7e5e0ae9b3997688f309a340d0203010001'),
               ('value', 50)])]} 

In [8]: txn=make_transaction(alice_wallet['address'], alice_wallet['private_key'], bob_wallet['address'], 10)
   ...: 
   ...: sign = txn.get('signature')
   ...: 
   ...: sender = txn.get('transaction').get('sender_address')
   ...: 
   ...: reciver = txn.get('transaction').get('recipient_address')
   ...: 
   ...: value = txn.get('transaction').get('value')
   ...: 

In [9]: print new_transaction(a, r, v, s)

In [9]: print new_transaction(sender, reciver, value, sign)
{'message': 'Transaction will be added to Block 3'}



```


### License

See the [LICENSE](LICENSE) file for license rights and limitations (MIT).
