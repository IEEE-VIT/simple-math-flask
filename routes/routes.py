from flask import Flask, render_template, request, Blueprint

router = Blueprint("router", __name__)

@router.route("/")
def start():
    return render_template('index.html')

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return
