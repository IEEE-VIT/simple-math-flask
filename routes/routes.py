from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/exponent", methods=["POST"])
def exponent():
    e=2.71828
    y=int(input("enter the value of the power"))
    t=e**y
    return(t)
