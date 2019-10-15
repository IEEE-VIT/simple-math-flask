from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/AGP", methods=["POST"])
def AGP():
    r=int(input("enter the value of common ratio "))
    a=int(input("enter the vlaue of first term"))
    d=int(input("enter the value of the common difference"))
    sum1=a/(1-r)
    sum2=(d*r)/(1-r)**2
    total=sum1+sum2
    return(total)
