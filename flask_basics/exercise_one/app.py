## Simple web app with home and about page

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/about")
def about_page():
    return render_template('about.html')

