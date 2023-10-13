from http import HTTPStatus
from flask import Blueprint, request, jsonify

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return 

@router.route("multiply",methods=["POST"])
def multiply():
    #Add logic here
    return

@router.route("/division",methods=['POST'])
def division():
    #Add logic here
    return

@router.route("/matrixaddition", methods=['POST'])
def matrix_addition():
    # Checking if request body is of correct format
    try:
        body = request.json
        data = body['data']
        assert isinstance(data, dict)
    except Exception:
        return jsonify({
            "result": None,
            "meta": { "error": "The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }" }
        }), HTTPStatus.BAD_REQUEST
    
    # Checking if operand keys in data dictionary is named properly
    for i in range(1, len(data.keys())+1):
        if f"param{i}" not in data:
            return jsonify({
                "result": None,
                "meta": { "error": "The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }" }
            }), HTTPStatus.BAD_REQUEST
    
    # Checking if there are atleast 2 operands
    if len(data.keys()) < 2:
        return jsonify({
            "result": None,
            "meta": { "error": "Matrix Addition requires atleast 2 operands" }
        }), HTTPStatus.BAD_REQUEST

    return "Matrix Addition Route"
