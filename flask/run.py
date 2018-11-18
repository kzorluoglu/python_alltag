# coding=utf-8
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():

    template = render_template(
        "index.html",
        title = "Welcome to Flask",
        name = request.args.get("name"),
        age = request.args.get("age")
    )
    return template

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
