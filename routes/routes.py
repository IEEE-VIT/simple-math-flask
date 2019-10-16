from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

#sanjay made this changes
@router.route("/hello")
def hello():
    return "Hactober is cool!. :)"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return
