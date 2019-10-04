from flask import Blueprint, request

router = Blueprint("router", __name__)


@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"


@router.route("/add", methods=["POST"])
def add():
    first_number = request.form['FirstNumber']
    second_number = request.form['SecondNumber']
    result = first_number + second_number
    return result
