from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"
#copied mayanks change to learn about github and to make PR's

@router.route("/HELLO")
def HELLO():
    return "hacktoberfest is cool!)"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return
print("this is my first pull request")
