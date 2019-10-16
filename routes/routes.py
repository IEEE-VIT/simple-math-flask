from flask import Blueprint

router = Blueprint("router", __name__)

#Tesla made this
@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/hello")
def hello():
return "Hactoberfest is cool!"

@router.route("/add", methods=["POST"])
def add():
    a=int(input("Enter the first number")
    b=input("Enter the second number")
    c=a+b
    print(c)
    # Add logic here
    return
