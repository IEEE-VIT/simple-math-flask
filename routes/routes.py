from flask import Blueprint,json,request

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():

    if request.get_json():
        args = json.loads(request.get_json())      # Loading the array from request
        if isinstance(args,list) or isinstance(args,int):
            return str(sum(args))
        else:
            return str(args) + ' is not a valid input'
    else:
        return 'No input was given'