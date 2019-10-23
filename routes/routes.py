from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return " Yaaahooooo !!! :)"


@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return
    x = request.form.data.param1
    y = request.form.data.param2

    summation = x+y

    res = {
        result: summation,
        meta: {
            message: "enter 2 nos : "
        }
    }
    return res
