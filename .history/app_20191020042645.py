from flask import Flask
from flask_cors import CORS
from routes.routes import router

PORT = 5000

app = Flask(__name__)
CORS(app)

app.register_blueprint(router, url_prefix="/math")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)