from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("infiniteGP", methods=["POST"])
def infiniteGP():
   a=int(input("enter the first term of the infinite GP"))
   r=int(input("enter the value of common ratio"))
   if(r==1):
        print("invalid input please try again")
   else:
        s=a/(1-r)

    return(s)
