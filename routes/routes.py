from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"
#chirag made this change
@router.route("/hello")
def hello():
    return "Hacktober fest is cool!! :)"

@router.route("/add", methods=["POST"])
def add():
    #a+b=c
    return
