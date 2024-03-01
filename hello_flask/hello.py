from flask import Flask

app = Flask(__name__)

print(__name__)


@app.route("/")
def hello_world():
    return ("<h1 style='text-align: center'>Hello, World!</h1> "
            "<p>This is a paragraph</p>"
            "<img src='https://media0.giphy.com/media/11kXFNRcZBFgwo/200.webp?cid"
            "=790b76116dv6wicy7sea14dn7uhbuidhdx41vodva1bt3x5m&ep=v1_gifs_search&rid=200.webp&ct=g' width='200px'>")


def make_bold(func):
    def wrapper():
        t = func()
        return f"<b>{t}</b>"

    return wrapper


def make_italic(func):
    def wrapper():
        t = func()
        return f"<em>{t}</em>"

    return wrapper


def make_underlined(func):
    def wrapper():
        t = func()
        return f"<u>{t}</u>"

    return wrapper


@app.route("/bye")
@make_bold
@make_italic
@make_underlined
def say_bye():
    return "Bye!"


@app.route("/username/<name>")
def greet(name):
    return f"<p>Hello {name}!!</p>"


if __name__ == "__main__":
    app.run(debug=True)
