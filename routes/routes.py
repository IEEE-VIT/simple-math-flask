from flask import Blueprint
from flask import request


router = Blueprint("router", __name__)


@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"


@router.route("/add", methods=["POST"])
def add():
    '''POST data should be in this format
    {'numbers': '2,3,5,1'}
    key: numbers
    value: csv of the numbers to be added
    '''
    numbers_csv = request.form.get('numbers', '0')
    numbers = list(map(int, numbers_csv.split(',')))
    _sum = sum(numbers)
    return f'Sum of {numbers} = {_sum}'