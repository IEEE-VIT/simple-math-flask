from flask import Flask, request, jsonify
import math
import unittest

app = Flask(__name)

@app.route('/math/factorial', methods=['POST'])
def calculate_factorial():
    try:
        data = request.get_json()
        n = data['number']
        result = math.factorial(n)
        return jsonify({'result': result})
    except (KeyError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400

class TestFactorialEndpoint(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_valid_factorial_request(self):
        data = {'number': 5}
        response = self.app.post('/math/factorial', json=data)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 120)

    def test_invalid_factorial_request(self):
        data = {'num': 5}  # Invalid key
        response = self.app.post('/math/factorial', json=data)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['error'], 'Invalid input')

if __name__ == '__main__':
    app.run()
