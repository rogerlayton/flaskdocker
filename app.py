from flask import Flask, render_template
from datetime import datetime
from __init__ import create_app

app = create_app()


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
