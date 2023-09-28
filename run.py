#!/usr/bin/env python3

from flask import Flask
import time

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world!"


@app.route("/time")
def get_time():
    return time.asctime()


app.run(host="0.0.0.0", port=8080, debug=True)
