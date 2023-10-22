import os
import sys
import unittest

sys.path.append(os.getcwd())

from app import app


class AppTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_check(self):
        response = self.app.get('/math/check')
        self.assertEqual(response.data, b'Congratulations! Your app works. :)')

    # Add the test_cases for various functionality here

    def test_multiplication_request_format1(self):
        response = self.app.post('/math/multiply')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, param2: <value> } }')

    def test_multiplication_request_format2(self):
        response = self.app.post('/math/multiply', json={"data": {"foo": "bar"}})
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, param2: <value> } }')

    def test_multiplication_request_format3(self):
        response = self.app.post('/math/multiply', json={"data": {}})
        self.assertEqual(response.json['meta']['error'], 'The request must contain exactly two operands.')

    def test_multiplication_operand_format(self):
        response = self.app.post('/math/multiply', json={"data": {
            "param1": "foo",
            "param2": "bar"
        }})
        self.assertEqual(response.json['meta']['error'], 'Operands must be integers/floats.')

    def test_multiplication_correctness(self):
        response = self.app.post('/math/multiply', json={"data": {
            "param1": 4,
            "param2": 5
        }})
        self.assertEqual(response.json['result'], 20)

    def test_exponentiation_request_format1(self):
        response = self.app.post('/math/exponentiation')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, param2: <value> } }')

    def test_exponentiation_request_format2(self):
        response = self.app.post('/math/exponentiation', json={"data": {"foo": "bar"}})
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, param2: <value> } }')

    def test_exponentiation_request_format3(self):
        response = self.app.post('/math/exponentiation', json={"data": {}})
        self.assertEqual(response.json['meta']['error'], 'The request must contain exactly two operands.')

    def test_exponentiation_operand_format(self):
        response = self.app.post('/math/matrixaddition', json={"data": {
            "param1": "foo",
            "param2": "bar"
        }})
        self.assertEqual(response.json['meta']['error'], 'Operands must be integers/floats.')

    def test_exponentiation_correctness(self):
        response = self.app.post('/math/matrixaddition', json={"data": {
            "param1": 5,
            "param2": 3
        }})
        self.assertEqual(response.json['result'], 125)

    def test_matrix_addition_request_format1(self):
        response = self.app.post('/math/matrixaddition')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }')

    def test_matrix_addition_request_format2(self):
        response = self.app.post('/math/matrixaddition', json={"data": {"foo": "bar"}})
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }')

    def test_matrix_addition_request_format3(self):
        response = self.app.post('/math/matrixaddition', json={"data": {}})
        self.assertEqual(response.json['meta']['error'], 'Matrix Addition requires atleast 2 operands')

    def test_matrix_addition_operand_format1(self):
        response = self.app.post('/math/matrixaddition', json={"data": {
            "param1": "foo",
            "param2": "bar"
        }})
        self.assertEqual(response.json['meta']['error'],
                         'Operands should be a matrix i.e list of lists of integers/floats')

    def test_matrix_addition_operand_format2(self):
        response = self.app.post('/math/matrixaddition', json={"data": {
            "param1": ["foo"],
            "param2": ["bar"]
        }})
        self.assertEqual(response.json['meta']['error'],
                         'Operands should be a matrix i.e list of lists of integers/floats')

    def test_matrix_addition_operand_format3(self):
        response = self.app.post('/math/matrixaddition', json={"data": {
            "param1": [["foo"]],
            "param2": [["bar"]]
        }})
        self.assertEqual(response.json['meta']['error'],
                         'Operands should be a matrix i.e list of lists of integers/floats')

    def test_matrix_addition_operand_format4(self):
        response = self.app.post('/math/matrixaddition', json={"data": {
            "param1": [[1], [2], [3]],
            "param2": [[1, 2, 3]]
        }})
        self.assertEqual(response.json['meta']['error'], 'Operands of matrix addition should be of same dimensions nxm')

    def test_matrix_addition_correctness(self):
        response = self.app.post('/math/matrixaddition', json={"data": {
            "param1": [
                [1, 1],
                [1, 1]
            ],
            "param2": [
                [2, 2],
                [2, 2]
            ],
            "param3": [
                [3, 3],
                [3, 3]
            ],
        }})
        self.assertEqual(response.json['result'], [
            [6, 6],
            [6, 6]
        ])

    # ------------------------------- SOLVE QUADRATIC EQUATION ----------------------------------------
    def test_quadratic_request_format1(self):
        """
        Test if '/math/quadraticequation' request contains data in json format
        """
        response = self.app.post('/math/quadraticequation')

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { a: <value>, b: <value>, '
                         'c: <value>} }')

    def test_quadratic_request_format2(self):
        """
        Test if '/math/quadraticequation' request contains the correct keys in data
        """
        response = self.app.post('/math/quadraticequation', json={"data": {"foo": "bar"}})

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { a: <value>, b: <value>, '
                         'c: <value>} }')

    def test_quadratic_operand_format(self):
        """
        Test if '/math/quadraticequation' request data keys are of correct format
        """
        response = self.app.post('/math/quadraticequation', json={"data": {
            "a": "2",
            "b": "1",
            "c": []
        }})

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'],
                         'Operands (a, b, c) should be either an int or a float')

    def test_quadratic_correctness(self):
        """
        Test if '/math/quadraticequation' request for correct output
        """
        response = self.app.post('/math/quadraticequation', json={"data": {
            "a": 1,
            "b": -3,
            "c": 2
        }})

        # assert statements
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json['result'], {'x1': 2.0, 'x2': 1.0})
        self.assertEqual(response.json['meta']['detail'], 'Two real and distinct solutions as (b^2 - 4ac) > 0')


if __name__ == '__main__':
    unittest.main()
