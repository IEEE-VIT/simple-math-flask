from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

#shreyansh has made this
@router.route("/hello")
def hello():
    return "hactoberfest is cool! :)"


@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return
