# This is our main file

# Requirements
import requests
import os
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random


"""
NETWORKING SECTION.
"""
def send_key(keystring):
    """
    This module sends a generated key to the server.
    """
    r = requests.post(
            url = "http://localhost:3000/savekey", 
            data = {
                "key":keystring
                }
            )
    print(r)


"""
KEYGEN SECTION
"""
# pad with spaces at the end of the text
# beacuse AES needs 16 byte blocks
def pad(s):
    block_size = 16
    remainder = len(s) % block_size
    padding_needed = block_size - remainder
    return s + padding_needed * ' '

# remove the extra spaces at the end
def unpad(s): 
    return s.rstrip()


"""
ENCRYPTION SECTION
"""
def encrypt(plain_text, password):
    # generate a random salt
    salt = os.urandom(AES.block_size)

    # generate a random iv
    iv = Random.new().read(AES.block_size)

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    # pad text with spaces to be valid for AES CBC mode
    padded_text = pad(plain_text)
    
    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_CBC, iv)

    # return a dictionary with the encrypted text
    return {
        'cipher_text': base64.b64encode(cipher_config.encrypt(padded_text)),
        'salt': base64.b64encode(salt),
        'iv': base64.b64encode(iv)
    }


"""
DRIVER SECTION
"""
if __name__ == "__main__":
    send_key("test")
