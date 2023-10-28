import os
import sys
import unittest

sys.path.append(os.getcwd())

from app import app


class TestDivision(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_division_request_format1(self):
        response = self.app.post('/math/division')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }')

    def test_division_request_format2(self):
        response = self.app.post('/math/division', json={"data": {"foo": "bar"}})
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }')

    def test_division_request_format3(self):
        response = self.app.post('/math/division', json={"data": {"param1": 1}})
        self.assertEqual(response.json['meta']['error'], 'Division requires exactly 2 operands')

    def test_division_request_format4(self):
        response = self.app.post('/math/division', json={"data": {"param1": 1, "param2": 2, "param3": 3}})
        self.assertEqual(response.json['meta']['error'], 'Division requires exactly 2 operands')

    def test_division_operand_format1(self):
        response = self.app.post('/math/division', json={"data": {
            "param1": "foo",
            "param2": "bar"
        }})
        self.assertEqual(response.json['meta']['error'], 'Operands should be a real number i.e. integer/float')

    def test_division_operand_format2(self):
        response = self.app.post('/math/division', json={"data": {
            "param1": 1,
            "param2": 0
        }})
        self.assertEqual(response.json['meta']['error'], 'Division by zero is not allowed')

    def test_division_correctness(self):
        response = self.app.post('/math/division', json={"data": {
            "param1": 3,
            "param2": 2,
        }})
        self.assertEqual(response.json['result'], 1.5)


if __name__ == '__main__':
    unittest.main()
