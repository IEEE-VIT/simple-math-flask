from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():                     # creating a UDF(User Defined Function) named check
    return "Congratulations! Your app works. :)"

# DSP made this change for a demo
@router.route("/hello")
def hello():
    return "Hacktoberfest is cool!"     # prints "Hacktoberfest is cool" on the output screen

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return
