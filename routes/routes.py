from flask import Blueprint,request,jsonify
import json

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

# Mayank made this
@router.route("/hello")
def hello():
    return "Hacktoberfest is cool!"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return

@router.route("/multiply", methods=["POST"])
def multiply():
    req_data = json.loads(request.data)["data"]
    param1 = req_data["param1"]
    param2 = req_data["param2"]

    return jsonify({'result':param1*param2, meta: {"message":"successfully multiplied 2 numbers"}})
