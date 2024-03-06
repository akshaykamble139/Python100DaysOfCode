from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)
URL = "https://api.npoint.io/c790b4d5cab58020d391"


@app.route('/')
def home():
    random_num = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template("index.html", num=random_num, curr_year=year)


@app.route('/guess/<name>')
def guess(name):
    gender_response = requests.get("https://api.genderize.io/?name=" + name).json()["gender"]
    age_response = requests.get("https://api.agify.io/?name=" + name).json()["age"]
    return render_template(
        "guess.html",
        name=name,
        age=age_response,
        gender=gender_response
    )


@app.route("/blog/<num>")
def get_blog(num):
    print(type(num))
    response = requests.get(URL)
    data = response.json()
    return render_template("blog.html", posts=data)


if __name__ == "__main__":
    app.run(debug=True)
