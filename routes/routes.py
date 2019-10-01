from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    x = request.form.data.param1
    y = request.form.data.param2

    summation = (x+x)**y

    res = {
        result: summation,
        meta: {
            message: "sending twice of first number and then its power second number"
        }
    }
    return

