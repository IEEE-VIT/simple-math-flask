import os
import sys
import unittest

sys.path.append(os.getcwd())

from app import app


class TestFactorial(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_factorial_request_format1(self):
        response = self.app.post('/math/factorial')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value> } }')

    def test_factorial_request_format2(self):
        response = self.app.post('/math/factorial', json={"data": {"foo": "bar"}})
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value> } }')

    def test_factorial_request_format3(self):
        response = self.app.post('/math/factorial', json={"data": {}})
        self.assertEqual(response.json['meta']['error'], 'The request must contain exactly one operand.')

    def test_factorial_operand_format(self):
        response = self.app.post('/math/factorial', json={"data": {
            "param1": "foo"
        }})
        self.assertEqual(response.json['meta']['error'], 'Operand must be integer only.')

    def test_factorial_operand_format(self):
        response = self.app.post('/math/factorial', json={"data": {
            "param1": -5
        }})
        self.assertEqual(response.json['meta']['error'], 'Operand must be positive integer only.')

    def test_factorial_correctness(self):
        response = self.app.post('/math/factorial', json={"data": {
            "param1": 5
        }})
        self.assertEqual(response.json['result'], 120)


if __name__ == '__main__':
    unittest.main()
