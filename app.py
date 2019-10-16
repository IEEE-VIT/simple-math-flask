from flask import Flask,render_template
from flask_cors import CORS
from routes.routes import router

PORT = 5000

app = Flask(__name__)
CORS(app)

app.register_blueprint(router, url_prefix="/math")

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=PORT)