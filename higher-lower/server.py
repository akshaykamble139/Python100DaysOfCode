from flask import Flask
import random
app = Flask(__name__)

answer = random.randint(0,9)
print(f"answer = {answer}")
@app.route("/")
def hello():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src = 'https://media4.giphy.com/media/l378khQxt68syiWJy/giphy.webp?cid=ecf05e47k3mxqehueuiqygqctd05ql90v104uxjogekjnhrw&ep=v1_gifs_search&rid=giphy.webp&ct=g'>")


@app.route("/<int:number>")
def guess_the_number(number):
    if number == answer:
        return ("<h1 style = 'color:green'><b>You found me!</b><h1>"
                "<img src = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")
    elif number < answer:
        return ("<h1 style = 'color:red'><b>Too low, try again!</b><h1>"
                "<img src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")

    return ("<h1 style = 'color:purple'><b>Too high, try again!</b><h1>"
            "<img src = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")


if __name__ == "__main__":
    app.run(debug=True)
