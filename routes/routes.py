from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():
    x = request.form.data.param1
    y = request.form.data.param2

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i

    res = {
        result: hcf,
        meta: {
            message: "sending addition of two numbers"
        }
    }
    return
