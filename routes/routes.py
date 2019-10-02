from flask import Blueprint, jsonify, make_response, request, json
from math import log, exp

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return


@router.route("/logarithm", methods=["POST"])
def logarithm():
    """ Returns a logarithm of a number with desired base.
    Args:
        number (:obj:`float`): A number to calculate logarithm for.
        base (:obj:`int`): Base of a logarithm. Optional argument. If omitted, function returns a natural logarithm
        of a given number.
    """
    data = request.json
    print(data)

    if not data:
        return json.dumps({'error': 'No input was provided.'})

    number = data.get("number")
    base = data.get("base", None)
    if not number:
        return json.dumps({'error': 'No number to calculate a logarithm was provided.'})

    return {"result": log(number, base)} if base else {"result": log(number)}
