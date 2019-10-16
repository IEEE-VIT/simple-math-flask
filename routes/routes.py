from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return
#Archisman made this
router = Blueprint("router", __name__)

@router.route("/hello")
def hello():
    return "Hactober is cool"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return
