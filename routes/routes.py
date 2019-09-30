from flask import Blueprint, request, jsonify

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():
    """API that returns sum of given list of numbers

    Input: {'numbers':[1,2,3,4]}
    
    Returns:
        str -- sum of numbers in string format
    """
    data = request.json
    numbers = data.get('numbers', [])
    return str(sum(numbers))