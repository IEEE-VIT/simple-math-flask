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


@router.route("multiply", methods=["POST"])
def multiply():
    # Checking if request body is of correct format
    try:
        body = request.json
        data = body['data']
        assert isinstance(data, dict)
    except Exception:
        return jsonify({
            "result": None,
            "meta": {
                "error": "The request must be a JSON of the following format: { data: { param1: <value>, param2: <value> } }"}
        }), HTTPStatus.BAD_REQUEST

    # Checking if operand keys in data dictionary is named properly
    for i in range(1, len(data.keys()) + 1):
        if f"param{i}" not in data:
            return jsonify({
                "result": None,
                "meta": {
                    "error": "The request must be a JSON of the following format: { data: { param1: <value>, param2: <value> } }"}
            }), HTTPStatus.BAD_REQUEST

    # Checking if there are 2 operands
    if len(data.keys()) != 2:
        return jsonify({
            "result": None,
            "meta": {"error": "The request must contain exactly two operands."}
        }), HTTPStatus.BAD_REQUEST

    # Checking if operands are of the correct type
    if (not isinstance(data["param1"], int) and not isinstance(data["param1"], float)) or (
            not isinstance(data["param2"], int) and not isinstance(data["param2"], float)):
        return jsonify({
            "result": None,
            "meta": {"error": "Operands must be integers/floats."}
        }), HTTPStatus.BAD_REQUEST

    # Result of Multiplication
    result = data["param1"] * data["param2"]

    return jsonify({
        "result": result,
        "meta": {}
    }), HTTPStatus.OK


@router.route("/division", methods=['POST'])
def division():
    # Add logic here
    return


@router.route("/exponentiation", methods=['POST'])
def exponentiation():
    # Checking if request body is of correct format
    try:
        body = request.json
        data = body['data']
        assert isinstance(data, dict)
    except Exception:
        return jsonify({
            "result": None,
            "meta": {
                "error": "The request must be a JSON of the following format: { data: { param1: <value>, param2: <value> } }"}
        }), HTTPStatus.BAD_REQUEST

    # Checking if operand keys in data dictionary is named properly
    for i in range(1, len(data.keys()) + 1):
        if f"param{i}" not in data:
            return jsonify({
                "result": None,
                "meta": {
                    "error": "The request must be a JSON of the following format: { data: { param1: <value>, param2: <value> } }"}
            }), HTTPStatus.BAD_REQUEST

    # Checking if there are 2 operands
    if len(data.keys()) != 2:
        return jsonify({
            "result": None,
            "meta": {"error": "The request must contain exactly two operands."}
        }), HTTPStatus.BAD_REQUEST

    # Checking if operands are of the correct type
    if (not isinstance(data["param1"], int) and not isinstance(data["param1"], float)) or (
            not isinstance(data["param2"], int) and not isinstance(data["param2"], float)):
        return jsonify({
            "result": None,
            "meta": {"error": "Operands must be integers/floats."}
        }), HTTPStatus.BAD_REQUEST

    # Result of exponentiation
    result = data["param1"] ** data["param2"]

    return jsonify({
        "result": result,
        "meta": {}
    }), HTTPStatus.OK


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
            "meta": {
                "error": "The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }"}
        }), HTTPStatus.BAD_REQUEST

    # Checking if operand keys in data dictionary is named properly
    for i in range(1, len(data.keys()) + 1):
        if f"param{i}" not in data:
            return jsonify({
                "result": None,
                "meta": {
                    "error": "The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }"}
            }), HTTPStatus.BAD_REQUEST

    # Checking if there are atleast 2 operands
    if len(data.keys()) < 2:
        return jsonify({
            "result": None,
            "meta": {"error": "Matrix Addition requires atleast 2 operands"}
        }), HTTPStatus.BAD_REQUEST

    # Checking if operand is of the correct format
    for i in range(1, len(data.keys()) + 1):
        if not isinstance(data[f'param{i}'], list) or len(data[f'param{i}']) == 0:
            return jsonify({
                "result": None,
                "meta": {"error": "Operands should be a matrix i.e list of lists of integers/floats"}
            }), HTTPStatus.BAD_REQUEST

        for row in data[f'param{i}']:
            if not isinstance(row, list) or len(row) == 0:
                return jsonify({
                    "result": None,
                    "meta": {"error": "Operands should be a matrix i.e list of lists of integers/floats"}
                }), HTTPStatus.BAD_REQUEST

            for el in row:
                if not isinstance(el, int) and not isinstance(el, float):
                    return jsonify({
                        "result": None,
                        "meta": {"error": "Operands should be a matrix i.e list of lists of integers/floats"}
                    }), HTTPStatus.BAD_REQUEST

    # Checking if all operands are of the same dimensions
    n = len(data['param1'])
    m = len(data['param1'][0])
    for i in range(1, len(data.keys()) + 1):
        if len(data[f'param{i}']) != n:
            return jsonify({
                "result": None,
                "meta": {"error": "Operands of matrix addition should be of same dimensions nxm"}
            }), HTTPStatus.BAD_REQUEST

        for row in data[f'param{i}']:
            if len(row) != m:
                return jsonify({
                    "result": None,
                    "meta": {"error": "Operands of matrix addition should be of same dimensions nxm"}
                }), HTTPStatus.BAD_REQUEST

    # Calculating result of matrix addition
    result_mat = [[0 for j in range(m)] for i in range(n)]
    for k in range(1, len(data.keys()) + 1):
        for i in range(n):
            for j in range(m):
                result_mat[i][j] += data[f'param{k}'][i][j]

    return jsonify({
        "result": result_mat,
        "meta": {}
    }), HTTPStatus.OK
