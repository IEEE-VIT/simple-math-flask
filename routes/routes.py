from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():
    val1 = request.form['val1']
    val2 = request.form['val2']
    add = val1 + val2
    return flask.jsonify({'data':f'<p>The result is: {val1+val2}</p>'})