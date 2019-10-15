from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/slope", methods=["POST"])
def slope():
    m1=int(input('enter the value of slope of line 1 '))
    m2=int(input('enter the value of slope of line 2 '))
    if(m1*m2==-1):
         t=print("line 1 and line 2 are perpendicular to each other ")
    elif(m1==m2):
        t=print('line 1 and line 2 are parallel to each other')
    else:
        t=print('no definite relation bertween line 1 & 2')
    return(t)
