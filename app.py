from flask import Flask, render_template
from datetime import datetime

app = Flask (__name__)


# Replace the existing home function with the one below
@app.route("/")
def home():
    return render_template("home.html")


# New functions
@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")

'''
@app.route("/")
def start():
    return "Hello, Flask!"
'''

'''
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
    '''
