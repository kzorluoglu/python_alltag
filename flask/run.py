# coding=utf-8
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    items = ['Apple', 'Orange', 'Banana']
    template = render_template("index.html", name="Koray", items=items)
    return template

if __name__ == "__main__":
    app.run()
