from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return

@route.route("/solve", methods=["POST"])
 def solve(coeffList):
        """
        Pass a list of coeff (a,b,c) , returns 2 roots
        """
        import cmath
        d = (coeffList[1]**2) - (4*coeffList[0]*coeffList[2])
        
        sol1 = (-coeffList[1]-cmath.sqrt(d))/(2*a)
        sol2 = (-coeffList[1]+cmath.sqrt(d))/(2*a)
        return sol1,sol2
