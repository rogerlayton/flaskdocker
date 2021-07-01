from flask import render_template, Blueprint


main = Blueprint('main', __name__)


# Replace the existing home function with the one below
@main.route("/")
def home():
    return render_template("home.html")


# New functions
@main.route("/about/")
def about():
    return render_template("about.html")


@main.route("/contact/")
def contact():
    return render_template("contact.html")
