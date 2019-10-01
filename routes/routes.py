from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return
@app.route('/', methods=['GET', 'POST'])
def home():
    form = investment()

    if request.method == 'POST': 
        return A + B

    elif request.method == 'GET':
        return render_template('home.html', form=form)
