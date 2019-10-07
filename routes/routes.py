from flask import Blueprint
from flask import jsonify, request
router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route('/add', methods = ['POST'])
def add():

    result = {
        'result' : None,
        'meta' : None
    }
    data_in = request.json['data']
    if not data_in:
        result['meta'] = "no json data was provided."
    values = []
    for i in data_in:
        values.append(data_in[i])
        result['result'] = sum(values)
    return jsonify(result)

# @ router.route('/subtract', methods = ['POST'])
# def subtract():
#     data_in = request.json['data']
#     values = []
#     for i in data_in:
        