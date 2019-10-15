from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/highest_common_factor", methods=["POST"])
def highest_common_factor():
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    g=b
    if b>=a:
        g=a
    
    for j in range(g,0,-1):
        if a%j==0 and b%j==0:
            break
            
    return j
