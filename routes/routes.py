from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/least_common_multiple", methods=["POST"])
def least_common_multiple():
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
   
    g=a
    if b>=a:
        g=b
        
    l=a*b+1  
    
    for i in range(g,l,1):
        if i%a==0 and i%b==0:
            break
            
    return i



                
