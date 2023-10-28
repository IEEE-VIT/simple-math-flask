from http import HTTPStatus

from flask import jsonify, request


class MultiplyViews:
    @staticmethod
    def multiply_two_numbers():
        # Checking if request body is of correct format
        try:
            body = request.json
            data = body['data']
            assert isinstance(data, dict)
        except Exception:
            return jsonify({
                "result": None,
                "meta": {
                    "error": "The request must be a JSON of the following format: { data: { param1: <value>, param2: "
                             "<value> } }"}
            }), HTTPStatus.BAD_REQUEST

        # Checking if operand keys in data dictionary is named properly
        for i in range(1, len(data.keys()) + 1):
            if f"param{i}" not in data:
                return jsonify({
                    "result": None,
                    "meta": {
                        "error": "The request must be a JSON of the following format: { data: { param1: <value>, "
                                 "param2: <value> } }"}
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
