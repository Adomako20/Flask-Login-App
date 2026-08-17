from flask import Flask, render_template, redirect, url_for
from auth import auth as auth_bp


# creating flask app
app = Flask(__name__)

# registering blueprints
app.register_blueprint(auth_bp)


# configs
app.secret_key = "thisissecret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"


@app.route("/")
def index():

    return render_template("index.html")


if __name__ == "__main__":

    app.run(debug=True)