from flask import Blueprint,json,request

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():
    args = json.loads(request.get_json())      # Loading the array from request
    return sum(args)   
