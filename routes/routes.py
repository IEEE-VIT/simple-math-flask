from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

# This change is made by Rithvik
@router.route("/Hello")
def check():
    return "Hacktoberfest is cool. :)"

@router.route("/add", methods=["POST"])
def add():
   
    # Add logic here
    return
