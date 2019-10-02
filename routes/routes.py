from flask import Blueprint, jsonify, make_response, request

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return

@router.route("/power", methods=["POST"])
def power():
    data = request.json
    if not data:
        return make_response(jsonify({
            'error': "Input expected!"
        }), 400)
    
    base = request.json.get("base")
    exponent = request.json.get("exponent", 0)
    if not base:
        return make_response(jsonify({
            "error": "Base value expected!"
        }), 400)
    
    return { "result": base ** exponent }