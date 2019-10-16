from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

# copied text

@router.route("/hello")
def hello():
    return "hackotberfeast :)"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return
