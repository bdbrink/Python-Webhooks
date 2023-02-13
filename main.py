# /usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

# decorator for the api the local host is serving
@app.route("/webhookcallback", methods=["POST"])
def hook():
    print(request.data)
    return "This is a response"

@app.route("/add", methods=["PUT"])
def add():
    print(request.data)
    return f"This is a response and {request.data}"

if __name__ == "__main__":
    app.run()