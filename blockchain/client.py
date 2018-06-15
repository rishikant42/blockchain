from binascii import hexlify, unhexlify
from collections import OrderedDict

import Crypto
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


class Wallet:
    def new_wallet(self):
        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator)

        private_key = key.exportKey(format='DER')
        public_key = key.publickey().exportKey(format='DER')

        response = {
            'private_key': hexlify(private_key).decode('ascii'),
            'address': hexlify(public_key).decode('ascii'),
        }
        return response


class Transaction:
    def __init__(self, sender_address, sender_pvt_key, recipient_address, value):
        self.sender_addresss = sender_address
        self.sender_pvt_key = sender_pvt_key
        self.recipient_address = recipient_address
        self.value = value

    # def __getattr__(self, attr):
    #     return self.data[attr]

    def to_dict(self):
        return OrderedDict({'sender_address': self.sender_addresss,
                            'recipient_address': self.recipient_address,
                            'value': self.value})

    def sign_transaction(self):
        private_key = RSA.importKey(unhexlify(self.sender_pvt_key))
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return hexlify(signer.sign(h)).decode('ascii')


def make_wallet():
    w = Wallet()
    new_wallet = w.new_wallet()
    return new_wallet

def make_transaction(sender_address, sender_pvt_key, recipient_address, value):
    transaction = Transaction(sender_address, sender_pvt_key, recipient_address, value)
    response = {
        'transaction': transaction.to_dict(),
        'signature': transaction.sign_transaction(),
    }
    return response
