# Blockchain

A blockchain is a continuously growing list of records, called blocks, which are linked and secured using cryptography
---

### Features:
```
* Blockchain Client
* Make Wallet
* Make Transaction
```

### Examples:

```
In [1]: from blockchain.client import make_wallet, make_transaction                                                        
                                                                                                                           
In [2]: make_wallet()                                                                                                      
Out[2]:                                                                                                                    
{'address': u'30819f300d06092a864886f70d010101050003818d0030818902818100faca1273711024f5fc37dcd7a435296d632b42a7bcb5fa2f4f5
8f046be37b40d286e5db554039281396f623c26397ee6a7bf67cbcd137aff14ca1ced22cb6045cade7994d2f63846ce6bae2c1bf5d5b27cfcece2f9c066
b7f6f03c854dcc3c2213cd9d882456d0d308ced64ccb01564d73bb7a7851025007669ae7d5c7c9d3550203010001',                             
 'private_key': u'3082025b02010002818100faca1273711024f5fc37dcd7a435296d632b42a7bcb5fa2f4f58f046be37b40d286e5db554039281396
f623c26397ee6a7bf67cbcd137aff14ca1ced22cb6045cade7994d2f63846ce6bae2c1bf5d5b27cfcece2f9c066b7f6f03c854dcc3c2213cd9d882456d0d308ced64ccb01564d73bb7a7851025007669ae7d5c7c9d3550203010001028180333956ef716684c621901f71843ebf89723a01d155002e6bbf5f4124$1f1babafd491da6cdd434f6640ed617c70ef3569568c9009d909f0cbee851643639281e71c13bb699a052fdf80dbf5829bfdc82c92a03b18e59376d772$e65a78175851801dda412823dfee42fc8331d8b919d820fa25eacca96f475eb4b968fd7622b9024100fd1b8c5093a7418d3af63bfa590c69b82af664d6$9a6ed292063cef95a01fc8a56bcfe7e9376c1c9119de02c06ef3672e4ddaeff70010a7dc73b9e8f93d3a98b024100fda7bdf4b3c23bf328ac584369551$67117bfa3b1540cc8b8995b186eee5d16b701ed7bdbfbfa91a5b59b16d12f5cf3395f9b30d1ee321f3618f66b16faf529f02402cf746ef4dbc0a264812$4c77e287963b1a64275db71df724e01cd54794c1f0c88aa5ce029dc9042e37153d11e8e42f3187bd5ca25a0d9b74cbce7c78430b74f02407f503839a01$f77b1e89126c136c4fa83fd058525b6280c7f0b09fc0381c45b6853a15d2f9713b712d34a1a73b830112c54de51ecac7f9fc6c954b57f7d4a9c5024044$fd3b9926ae71bbb6ac203db2d6577c5b0c9c4b05b17e368ebae0eb7bca03c331b073e261fd6cf8ede8381991833e4426eb53cd98f5a4ca7b8a36c3cf79$96'}

In [3]: w1 = make_wallet()

In [4]: w2 = make_wallet()

In [5]: make_transaction(w1['address'], w2['private_key'], w2['address'], 10)
Out[5]: 
{'signature': u'5c468536c0330ecdb938f9a29063e0283434e999ae8a743932507eb27745bb2445d2d79ba4afa749058a9061725e45de13a90424ea3c6cefae1ebf462c0524052405cc260b349db2bb6a6c679a17c31541da704354eefbf9b850a4914046e0120ae6cd2a6bc447012681014b0528f6e8f2bb81dd2741ffe2b7cc99abf74504db',
 'transaction': OrderedDict([('sender_address',
               u'30819f300d06092a864886f70d010101050003818d0030818902818100b3a54a6b310ed29255300c83903a9691736020128d065cbd43415fac7e7f0e0ad266aaab5117f8d9a10aa0c0d49bada4b22dbb8b880b3e9cd2ed1060d3db2ab35b8bcae138de8c90b3ace8efb79545c7822e752ae47f9b7b74f3aa42e16bd9b712347d175ca523726bba840c223e238a4e840866c9e3bad1b444b212978b44cf0203010001'),
              ('recipient_address',
               u'30819f300d06092a864886f70d010101050003818d0030818902818100a064b64a641bb3b91b36293549dcaf48729fbd01769c5961f22dc6bfc12490468a98b606fb3cea5fb1801e4a8ff3e41b3b955645e973affff29939966417991b3f5701c315db890aca31a36c8fdf0b7f44316ba5a79f9fd1e033dfaead895d956c74e963ae09bd25bb4e554d4923fff5c0cbd3f320dd61f42e899c563d5aac450203010001'),
              ('value', 10)])}
```

### License

See the [LICENSE](LICENSE) file for license rights and limitations (MIT).
