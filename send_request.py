# /usr/bin/env python3

import requests

def callback():
    # local host
    url = "http://127.0.0.1:5000/webhookcallback"

    r = requests.post(url)
    print(r.content)

def add_response():

    url = "http://127.0.0.1:5000/add"

    r = requests.put(url, "I'm adding this")
    print(r.content)

if __name__ == "__main__":
    callback()
    add_response()