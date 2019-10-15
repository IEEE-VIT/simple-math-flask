from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/solv2var", methods=["POST"])
def solv2var():
    import numpy as np

    a1=float(input("Enter 1st coeffecient of 1st equation:\n"))
    b1=float(input("Enter 2nd coeffecient of 1st equation:\n"))
    c1=float(input("Enter constant of 1st equation:\n"))
    a2=float(input("Enter 1st coeffecient of 2nd equation:\n"))
    b2=float(input("Enter 2nd coeffecient of 2nd equation:\n"))
    c2=float(input("Enter constant of 2nd equation:\n"))


    a = np.array([[a1,b1], [a2,b2]])
    b = np.array([c1,c2])
    t = np.linalg.solve(a, b)

    return(t[0],t[1])
