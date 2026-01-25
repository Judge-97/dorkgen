#!/usr/bin/env python3

from flask import Flask
from flask.templating import render_template_string

app = Flask(__name__)
template = "./index.html" if __file__.endswith(".py") else "/usr/local/share/dorkgen/index.html"

@app.route("/")
def root():
    with open(template, "r") as f:
        return render_template_string(f.read())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1234)