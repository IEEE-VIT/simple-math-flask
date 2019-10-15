from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/summation", methods=["POST"])
def summation():
    n=int(input("enter the value of numbers "))
    s1=(n*(n+1))/2 #sum of n numbers 

    return(s1)
