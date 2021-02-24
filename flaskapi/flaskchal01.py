#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route("/")
def land():
    return f"HomePage"

@app.route("/home")
def home():
    return f"This is HomePage"

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello fellow programmer, {name}"


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

