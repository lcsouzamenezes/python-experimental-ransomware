# This is our main file

# Requirements
import requests


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


if __name__ == "__main__":
    send_key("test")
