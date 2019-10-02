from flask import Blueprint,request
import json, functools

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return

@router.route("/product", methods=["POST"])
def product():
    result = {
        'result': None,
        'meta': None
    }

    # Works with multiple parameters

    if request.get_json():
        args = json.loads(request.get_json())
        args = [args['data'][i] for i in args['data']]
        result['result'] = functools.reduce(lambda x,y: x*y,args)
        return json.dumps(result)

    else:
        result['meta'] = 'No JSON provided'
        return json.dumps(result)

@router.route("/division", methods=["POST"])
def division():
    result = {
        'result': None,
        'meta': None
    }

    # Works with 2 parameters

    if request.get_json():
        args = json.loads(request.get_json())['data']
        result['result'] = args['param1']/args['param2']
        return json.dumps(result)

    else:
        result['meta'] = 'No JSON provided'
        return json.dumps(result)