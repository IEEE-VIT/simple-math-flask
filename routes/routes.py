from flask import Blueprint

router = Blueprint("router", __name__)

# I copied mayank's change to learn github
@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/hello")
def hello():
    return "Hacktober fest is KWEL !"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return
print('This is my first pull request')
