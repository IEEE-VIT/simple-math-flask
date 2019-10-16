from flask import Flask, render_template, request, Blueprint

router = Blueprint("router", __name__)

@router.route("/")
def start():
    return render_template('index.html')


#function to add
@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    n1 = int(request.form['num1'])
    n2 = int(request.form['num2'])
    return n1+n2


#function to subtract
@router.route("/sub", methods=["POST"])
def add():
    # Add logic here
    n1 = int(request.form['num1'])
    n2 = int(request.form['num2'])
    return n1-n2

#function to multiply
@router.route("/mul", methods=["POST"])
def add():
    # Add logic here
    n1 = int(request.form['num1'])
    n2 = int(request.form['num2'])
    return n1*n2

#function to divide (integer division)
@router.route("/div", methods=["POST"])
def add():
    # Add logic here
    n1 = int(request.form['num1'])
    n2 = int(request.form['num2'])
    return n1//n2
