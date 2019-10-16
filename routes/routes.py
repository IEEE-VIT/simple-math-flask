from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/hello")
def start():
    return "Hello world!"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return
