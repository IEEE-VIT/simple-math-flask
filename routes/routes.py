from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/factorial", methods=["POST"])
def factorial():
    a=int(input("Enter a number whose factorial you want to find:\n"))
    fact=1
    
    if a<0:
        print("Invalid Input!")
        
    elif type(a)==float:
        print("Invalid Input")
        
    else:
        for i in range (1,a+1,1):
            fact=fact*i
            
    return fact
