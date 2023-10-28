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


@router.route("/matrix-addition", methods=['POST'])
def matrix_addition():
    return AddViews.add_matrices()


@router.route("/matrixmultiplication", methods=['POST'])
def matrix_multiplication():
    return MultiplyViews.multiply_matrices()


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
