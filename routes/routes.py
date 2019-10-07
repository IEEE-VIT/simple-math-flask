from flask import Blueprint
from flask import jsonify, request, Response
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

@ router.route('/subtract', methods = ['POST'])
def subtract():
    result = {
        'result' : None,
        'meta' : None
    }
    if not request.json:
        result['meta'] = "please post some values"
        return jsonify(result)
    else:
        data_in = request.json['data']

    if not data_in:
        result['meta'] = "no json data was provided.."
        return jsonify(result)
    else:
        values = []
        for i in data_in:
            values.append(data_in[i])
    result['result'] = 0
    for i in values:
        result['result'] = i - result['result']
    return jsonify(result)

@router.route('/product', methods = ['POST'])
def product():
    result = {
        'result' : None,
        'meta' : None
    }
    if not request.json:
        result['meta'] = "please post some values"
        return jsonify(result)
    else:
        data_in = request.json['data']

    if not data_in:
        result['meta'] = "no json data was provided.."
        return jsonify(result)
    else:
        values = []
        for i in data_in:
            values.append(data_in[i])
    result['result'] = 1
    for i in values:
        result['result'] = i * result['result']
    
    return jsonify(result)


        