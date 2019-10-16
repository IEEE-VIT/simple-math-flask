from flask import Blueprint,request,jsonify
inport json
router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return
#changed 
@router.route("/hello")
def hello():
    return "hactober is cool. :)"
