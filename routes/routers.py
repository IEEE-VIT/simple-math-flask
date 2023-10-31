from flask import Blueprint

from routes.views import AddViews, MultiplyViews, DivideViews, EquationViews

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


@router.route("/matrix-multiplication", methods=['POST'])
def matrix_multiplication():
    return MultiplyViews.multiply_matrices()


@router.route("/quadratic-equation", methods=['POST'])
def solve_quadratic_equation():
    return EquationViews.quadratic_equation()


@router.route("/factorial", methods=["POST"])
def factorial():
    return MultiplyViews.calculate_factorial()


@router.route("/hcf-lcm", methods=['POST'])
def hcf_lcm():
    return MultiplyViews.calculate_hcf_lcm()
