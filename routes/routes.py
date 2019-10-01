from flask import Blueprint

router = Blueprint("router", __name__)


@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"


@router.route("/add", methods=["POST"])
def add():

    x = request.form.data.param1
    y = request.form.data.param2
    
    summation = x+y
    
    res = {
        result: summation,
        meta: {
            message: "sending addition of two numbers"
        }
    }
    return
