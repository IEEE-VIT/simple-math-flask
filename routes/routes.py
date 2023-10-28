from http import HTTPStatus

from flask import Blueprint, request, jsonify

from routes.views import AddViews, MultiplyViews, DivideViews

router = Blueprint("router", __name__)


@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"


@router.route("/add", methods=["POST"])
def add():
    return AddViews.add_two_numbers()


@router.route("multiply", methods=["POST"])
def multiply():
    return MultiplyViews.multiply_two_numbers()


@router.route("/division", methods=['POST'])
def division():
    return DivideViews.divide_two_numbers()


@router.route("/exponentiation", methods=['POST'])
def exponentiation():
    return MultiplyViews.exponent()


@router.route("/matrixaddition", methods=['POST'])
def matrix_addition():
    return AddViews.add_matrices()


@router.route("/matrixmultiplication", methods=['POST'])
def matrix_multiplication():
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
                "error": "The request must be a JSON of the following format: { matrices: [matrix_1, matrix_2, ..., "
                         "matrix_n] } Here matrix_1, matrix_2, ..., matrix_n must be list of lists"}
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
                "meta": {"error": "A matrix can't be empty or a matrix should be a list of lists of integers/floats"}
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
                "meta": {"error": "Matrix dimensions are not compatible for multiplication! i.e. The columns of first"
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


@router.route("/quadraticequation", methods=['POST'])
def solve_quadratic_equation():
    """
    Solves a quadratic equation of the form ax^2 + bx + c = 0 and returns the solution.
    It takes three values a, b and c (can be an integer or float) in data dictionary
    which represents the coefficients of quadratic equation and calculate the solution
    based on discriminant (b^2 - 4ac).
    """

    # Checking if request body is of correct format and contains the correct operand keys
    try:
        body = request.get_json()
        data = body['data']
        assert isinstance(data, dict)

        a = data['a']
        b = data['b']
        c = data['c']
    except Exception:
        return jsonify({
            "result": None,
            "meta": {
                "error": "The request must be a JSON of the following format: { data: { a: <value>, b: <value>,"
                         " c: <value>} }"}
        }), HTTPStatus.BAD_REQUEST

    # Checking if operand is of the correct format
    try:
        assert isinstance(a, int) or isinstance(a, float)
        assert isinstance(b, int) or isinstance(b, float)
        assert isinstance(c, int) or isinstance(c, float)
    except Exception:
        return jsonify({
            "result": None,
            "meta": {"error": "Operands (a, b, c) should be either an int or a float"}
        }), HTTPStatus.BAD_REQUEST

    # Calculate the discriminant (b^2 - 4ac).
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        # Two real and distinct solutions.
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        result = {'x1': x1, 'x2': x2}
        meta = "Two real and distinct solutions as (b^2 - 4ac) > 0"

    elif discriminant == 0:
        # One real solution (a repeated root).
        x = -b / (2 * a)
        result = {'x': x}
        meta = "One real solution as (b^2 - 4ac) = 0"

    else:
        # No real solution (complex roots).
        real_part = -b / (2 * a)
        imaginary_part = (-discriminant) ** 0.5 / (2 * a)
        result = {'real_part': real_part, 'imaginary_part': imaginary_part}
        meta = "No real solution, it contains complex roots as (b^2 - 4ac) < 0"

    return jsonify({
        "result": result,
        "meta": {
            "detail": meta
        }
    }), HTTPStatus.OK
