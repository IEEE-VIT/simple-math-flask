from flask import Blueprint
from flask import request
from flask import render_template

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST","GET"])
def add():
    # Add logic here
    if request.method == "POST":
        no1 = request.form['no1']
        no2 = request.form['no2']
        no3 = int(no1) + int(no2)
        return render_template('input.html', res= str(no3), op="Add")
    return render_template('input.html',res="",op="Add")

@router.route("/sub", methods=["POST","GET"])
def sub():
    # Add logic here
    if request.method == "POST":
        no1 = request.form['no1']
        no2 = request.form['no2']
        no3 = int(no1) - int(no2)
        return render_template('input.html', res= str(no3), op="Subtract")
    return render_template('input.html',res="", op="Subtract")

@router.route("/mul", methods=["POST","GET"])
def mul():
    # Add logic here
    if request.method == "POST":
        no1 = request.form['no1']
        no2 = request.form['no2']
        no3 = int(no1) * int(no2)
        return render_template('input.html', res= str(no3), op="Multiply")
    return render_template('input.html',res="",op="Multiply")

@router.route("/div", methods=["POST","GET"])
def div():
    # Add logic here
    if request.method == "POST":
        no1 = request.form['no1']
        no2 = request.form['no2']
        no3 = int(no1) / int(no2)
        return render_template('input.html', res= str(round(no3,2)), op="Divide")
    return render_template('input.html',res="", op="Divide")


