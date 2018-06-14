from binascii import hexlify

import Crypto
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

def create_new_wallet():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)

    private_key = key.exportKey(format='DER')
    public_key = key.publickey().exportKey(format='DER')

    response = {
        'private_addr': hexlify(private_key).decode('ascii'),
        'public_addr': hexlify(public_key).decode('ascii'),
        }

    return response
