import os
import sys
import unittest

sys.path.append(os.getcwd())

from app import app


class TestAddition(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_addition_request_format1(self):
        response = self.app.post('/math/add')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, '
                         'param2: <value> } }')

    def test_addition_request_format2(self):
        response = self.app.post('/math/add', json={"data": {"foo": "bar"}})
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, '
                         'param2: <value> } }')

    def test_addition_request_format3(self):
        response = self.app.post('/math/add', json={"data": {}})
        self.assertEqual(response.json['meta']['error'], 'The request must contain exactly two operands.')

    def test_addition_operand_format(self):
        response = self.app.post('/math/add', json={"data": {
            "param1": "foo",
            "param2": "bar"
        }})
        self.assertEqual(response.json['meta']['error'], 'Operands must be integers/floats.')

    def test_addtion_correctness(self):
        response = self.app.post('/math/add', json={"data": {
            "param1": 7,
            "param2": 3
        }})
        self.assertEqual(response.json['result'], 10)


if __name__ == '__main__':
    unittest.main()
