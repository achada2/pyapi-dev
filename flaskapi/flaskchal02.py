#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route("/")
def land():
    return f"HomePage"

@app.route("/home")
def home():
    return f"This is HomePage"

@app.route("/hello/<pname>")
def hello_name(pname):
    return f"Hello fellow programmer, {pname}"

@app.route("/user/<name>")
def hello_user(name):
    if name =="admin":
        return redirect(url_for("hello_name",pname = name)) #you'll need to return the value of name in your redirect
    else:
        return f"Hello NON-admin programmer"



if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

