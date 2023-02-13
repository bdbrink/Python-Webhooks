# /usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/webhookcallback", methods=["POST"])
def hook():
    print(request.data)
    return "I'm a response"

if __name__ == "__main__":
    app.run()