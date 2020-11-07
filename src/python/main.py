# This is our main file

# Requirements
import requests
import os
import pyAesCrypt

"""
NETWORKING SECTION.
"""
def send_key(keystring):
    """
    This module sends a generated key to the server.
    """
    try:

        r = requests.post(
                url = "http://localhost:3000/savekey", 
                data = {
                    "key":keystring
                    }
                )
    except:
        print("Failed to reach the server, so aborted")
    print(r)


"""
KEYGEN SECTION
"""


"""
ENCRYPTION SECTION
"""
bufferSize = 64*1024
def encrypt(password, filepath):
    pyAesCrypt.encryptFile(filepath, filepath+".aes", password, bufferSize)




"""
DECRYPTION SECTION
"""
def decrypt(password, filepath):
    pyAesCrypt.decryptFile(filepath, filepath[:-4], password, bufferSize)


"""
DRIVER SECTION
"""
if __name__ == "__main__":
    
    #encrypt("password", "./testing/test.txt")
    decrypt("password", "./testing/test.txt.aes")
