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
    except Exception:
        return jsonify({
            "result": None,
            "meta": { "error": "The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }" }
        }), HTTPStatus.BAD_REQUEST
    
    return "Matrix Addition Route"
