from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return 

@router.route("multiply",methods=["POST"])
def multiply():
    #Add logic here
    return

@router.route("/division",methods=['POST'])
def division():
    #Add logic here
    return
