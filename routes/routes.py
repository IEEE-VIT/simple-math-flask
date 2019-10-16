from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/HEY")
def HEY():
    return "how you doing.. :)"
#hactoberfest is cool 

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return
