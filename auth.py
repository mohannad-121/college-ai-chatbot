from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

auth = Blueprint("auth", __name__)

@auth.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()

        if not user:
            error = "User does not exist"
        elif not check_password_hash(user.password, request.form["password"]):
            error = "Wrong password"
        else:
            login_user(user)
            return redirect(url_for("chat"))

    return render_template("login.html", error=error)


@auth.route("/register", methods=["POST"])
def register():
    user = User(
        username=request.form["username"],
        password=generate_password_hash(request.form["password"])
    )
    db.session.add(user)
    db.session.commit()
    return redirect("/login")

@auth.route("/logout")
def logout():
    logout_user()
    return redirect("/")
