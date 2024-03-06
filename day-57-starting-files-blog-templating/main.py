from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
URL = "https://api.npoint.io/c790b4d5cab58020d391"
all_posts = []


@app.route('/')
def home():
    global all_posts
    response = requests.get(URL).json()
    all_posts.clear()
    for data in response:
        all_posts.append(Post(data))
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:num>')
def get_post(num):
    if all_posts:
        curr_post = all_posts[num - 1]
    else:
        response = requests.get(URL).json()
        curr_post = Post(response[num - 1])

    return render_template("post.html", post=curr_post)


if __name__ == "__main__":
    app.run(debug=True)
