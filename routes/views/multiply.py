from http import HTTPStatus
from math import gcd

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

    @staticmethod
    def exponent():
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

        # Result of exponentiation
        result = data["param1"] ** data["param2"]

        return jsonify({
            "result": result,
            "meta": {}
        }), HTTPStatus.OK

    @staticmethod
    def multiply_matrices():
        """
            Multiply two or more matrices and return the resultant matrix.
            It takes a list of matrices in request body. Each matrix should
            be a list of lists and contains only int or float values.
            """
        # Checking if request body is of correct format
        try:
            body = request.json
            matrices = body['matrices']
            assert isinstance(matrices, list)
        except Exception:
            return jsonify({
                "result": None,
                "meta": {
                    "error": "The request must be a JSON of the following format: { matrices: [matrix_1, matrix_2,"
                             " ..., matrix_n] } Here matrix_1, matrix_2, ..., matrix_n must be list of lists"}
            }), HTTPStatus.BAD_REQUEST

        # Checking if there are at least 2 matrices
        if len(matrices) < 2:
            return jsonify({
                "result": None,
                "meta": {"error": "At least two matrices are required for multiplication"}
            }), HTTPStatus.BAD_REQUEST

        # Checking if operand is of the correct format
        for matrix in matrices:
            if not isinstance(matrix, list) or not matrix:
                return jsonify({
                    "result": None,
                    "meta": {
                        "error": "A matrix can't be empty or a matrix should be a list of lists of integers/floats"}
                }), HTTPStatus.BAD_REQUEST

            for row in matrix:
                if not isinstance(row, list) or len(row) == 0:
                    return jsonify({
                        "result": None,
                        "meta": {"error": "A matrix row can't be Empty or A matrix row should be a list"}
                    }), HTTPStatus.BAD_REQUEST

                for el in row:
                    if not isinstance(el, int) and not isinstance(el, float):
                        return jsonify({
                            "result": None,
                            "meta": {"error": "A matrix row should contain either an int or float"}
                        }), HTTPStatus.BAD_REQUEST

        matrix_a = matrices[0]
        for matrix_b in matrices[1:]:
            rows_a, cols_a = len(matrix_a), len(matrix_a[0])
            rows_b, cols_b = len(matrix_b), len(matrix_b[0])

            if cols_a != rows_b:
                return jsonify({
                    "result": None,
                    "meta": {
                        "error": "Matrix dimensions are not compatible for multiplication! i.e. The columns of first"
                                 " matrix should be equal to the rows of 2nd matrix and so on."}
                }), HTTPStatus.BAD_REQUEST

            _result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

            for i in range(rows_a):
                for j in range(cols_b):
                    for k in range(cols_a):
                        _result[i][j] += matrix_a[i][k] * matrix_b[k][j]
            matrix_a = _result

        return jsonify({
            "result": matrix_a,
            "meta": {}
        }), HTTPStatus.OK

    @staticmethod
    def calculate_factorial():
        # Checking if request body is of correct format
        try:
            body = request.json
            data = body['data']
            assert isinstance(data, dict)
        except Exception:
            return jsonify({
                "result": None,
                "meta": {"error": "The request must be a JSON of the following format: { data: { param1: <value> } }"}
            }), HTTPStatus.BAD_REQUEST

        # Checking if operand keys in data dictionary is named properly
        for i in range(1, len(data.keys()) + 1):
            if f"param{i}" not in data:
                return jsonify({
                    "result": None,
                    "meta": {
                        "error": "The request must be a JSON of the following format: { data: { param1: <value> } }"}
                }), HTTPStatus.BAD_REQUEST

        # Checking if the operand is not more 1
        if len(data.keys()) != 1:
            return jsonify({
                "result": None,
                "meta": {"error": "The request must contain exactly one operand."}
            }), HTTPStatus.BAD_REQUEST

        # Checking if operand are of the correct type
        if not isinstance(data["param1"], int):
            return jsonify({
                "result": None,
                "meta": {"error": "Operand must be integer only."}
            }), HTTPStatus.BAD_REQUEST

        # Checking if the operand is less than zero
        if data['param1'] < 0:
            return jsonify({
                "result": None,
                "meta": {"error": "Operand must be positive integer only."}
            }), HTTPStatus.BAD_REQUEST

        # Result of factorial
        if data["param1"] == 0:
            result = 1

        else:
            result = 1
            for i in range(1, data["param1"] + 1):
                result *= i

        return jsonify({
            "result": result,
            "meta": {}
        }), HTTPStatus.OK

    @staticmethod
    def calculate_hcf_lcm():
        # Checking if request body is of correct format and contains the correct operand keys
        try:
            body = request.get_json()
            data = body['data']
            assert isinstance(data, dict)

            a = data['a']
            b = data['b']

        except Exception:
            return jsonify({
                "result": None,
                "meta": {
                    "error": "The request must be a JSON of the following format: { data: { a: <value>, b: <value>} }"
                }
            }), HTTPStatus.BAD_REQUEST

        # Checking if operand is of the correct format
        try:
            assert isinstance(b, int)
            assert isinstance(a, int)

        except Exception:
            return jsonify({
                "result": None,
                "meta": {"error": "Operands a, b should be either an int Only"}
            }), HTTPStatus.BAD_REQUEST

        # Changing the Negative Numbers to Positive.
        if a < 1:
            a = a * -1
        if b < 1:
            b = b * -1

        lcm = abs(a * b) // gcd(a, b)
        result = {"hcf": gcd(a, b), "lcm": lcm}

        return jsonify({
            "result": result,
            "meta": {}
        }), HTTPStatus.OK
