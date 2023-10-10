from flask import Blueprint, request, jsonify

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():
    try:
        data = request.get_json()
        num1 = data.get("num1")
        num2 = data.get("num2")
        result = num1 + num2
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@router.route("/multiply", methods=["POST"])
def multiply():
    try:
        data = request.get_json()
        num1 = data.get("num1")
        num2 = data.get("num2")
        result = num1 * num2
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@router.route("/division", methods=['POST'])
def division():
    try:
        data = request.get_json()
        num1 = data.get("num1")
        num2 = data.get("num2")
        if num2 == 0:
            return jsonify({"error": "Division by zero is not allowed"}), 400
        result = num1 / num2
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
