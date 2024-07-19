from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {'username' : "Jerry"}
    posts = [
        {'author' : {'username':'John'},
         'body': {'Beautiful day in Naija'}
         },
         {'author' : {'username':'Harry'},
         'body': {'Only the strong survives'}
         }

    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
