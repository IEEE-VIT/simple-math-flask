from http import HTTPStatus

from flask import jsonify, request


class DivideViews:
    @staticmethod
    def divide_two_numbers():
        # Checking if request body is of correct format
        try:
            body = request.json
            data = body['data']
            assert isinstance(data, dict)
        except Exception:
            return jsonify({
                "result": None,
                "meta": {
                    "error": "The request must be a JSON of the following format: { data: { param1: <value>, ... "
                             "param<n>: <value> } }"}
            }), HTTPStatus.BAD_REQUEST

        # Checking if operand keys in data dictionary is named properly
        for i in range(1, len(data.keys()) + 1):
            if f"param{i}" not in data:
                return jsonify({
                    "result": None,
                    "meta": {
                        "error": "The request must be a JSON of the following format: { data: { param1: <value>, ... "
                                 "param<n>: <value> } }"}
                }), HTTPStatus.BAD_REQUEST

        # Checking if there are exactly 2 operands
        if len(data.keys()) != 2:
            return jsonify({
                "result": None,
                "meta": {"error": "Division requires exactly 2 operands"}
            }), HTTPStatus.BAD_REQUEST

        # Checking if operand is of the correct format
        for i in range(1, len(data.keys()) + 1):
            if not isinstance(data[f'param{i}'], int) and not isinstance(data[f'param{i}'], float):
                return jsonify({
                    "result": None,
                    "meta": {"error": "Operands should be a real number i.e. integer/float"}
                }), HTTPStatus.BAD_REQUEST

        # Check if the divisor is zero
        if data['param2'] == 0:
            return jsonify({
                "result": None,
                "meta": {"error": "Division by zero is not allowed"}
            }), HTTPStatus.BAD_REQUEST

        div_res = data["param1"] / data["param2"]

        return jsonify({
            "result": div_res,
            "meta": {}
        }), HTTPStatus.OK
