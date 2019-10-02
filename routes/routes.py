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
    """ Takes the base, exponent as parameters
    and returns the base ^ exponent value

    sample input: json-> {"base": 2, "exponent": 3}
    sample output: json -> {"result": 8}
    """
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

    return {"result": base ** exponent} # equivalent to pow(base, exponent)


@router.route("/root", methods=["POST"])
def root():
    """ Takes the base, root as parameters
    and returns the base ^ (1/root) value (aka, nth root)

    sample input: json-> {"base": 16, "root": 4}
    sample output: json -> {"result": 2}
    """
    data = request.json
    if not data:
        return make_response(jsonify({
            'error': "Input expected!"
        }), 400)

    base = request.json.get("base")
    root = request.json.get("root", 2)
    if not base:
        return make_response(jsonify({
            "error": "Base value expected!"
        }), 400)
    return {"result": base ** (1/float(root))}