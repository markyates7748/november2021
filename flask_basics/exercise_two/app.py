## Trying with GET/POST

from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to this web app"

@app.route("/product/<item>")
def get_item(item):
    return f"This is the page for {str(item)}"

@app.route("/sale/<sale_id>")
def get_sale(sale_id=0):
    return f"This is the page for transaction {str(sale_id)}"

@app.route("/create/<first_name>/<last_name>")
def greeting(first_name=None, last_name=None):
    return f"Hello {first_name} {last_name}"

@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}"

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("success", name=user))
    else:
        user = request.args.get("nm")
        return redirect(url_for("success", name=user))