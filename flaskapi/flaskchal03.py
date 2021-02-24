#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/success/<name>")
def success(uname):
#    if uname = "Aditya" and passwd = "Really!"
    return f"Welcome {name}\n"

@app.route("/fail")
def fail():
    return f"LOGIN FAILED\n"

@app.route("/")
@app.route("/start")
def start():
    return render_template("postmaker1.html")

@app.route("/login", methods = ["POST"])
def login():
    if request.method == "POST":
            user = request.form.get("nm")
            pswd = request.form.get("pw")
            if user == "Aditya" and pswd == "Really!":
     return redirect(url_for("success", name = user))
    else:
        return redirect(url_for("fail"))  
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) 

