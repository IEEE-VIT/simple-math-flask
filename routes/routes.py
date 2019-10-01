from functools import reduce

from flask import Blueprint, jsonify, make_response, request

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return

@router.route('/multiply', methods=["POST"])
def multiply():
    """ Takes list of literals as input and
        returns the product of the literals

        Sample Input : { "input" : [1,2,3,4,5] }
        Sample Output : { "output" : 120 }
    """
    
    if not request.json:
        return make_response(jsonify({
            "error": "Input expected"
        }))
    numbers = request.json.get('input', [])
    try:
        output = reduce(lambda x, y: x * y, numbers)
    except:
        return make_response(jsonify({
            "error": "Invalid input, expected an iterable"
        }), 400)
    return jsonify({"output": output})