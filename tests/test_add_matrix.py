import os
import sys
import unittest

sys.path.append(os.getcwd())

from app import app


class TestAddMatrix(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_matrix_addition_request_format1(self):
        response = self.app.post('/math/matrix-addition')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }')

    def test_matrix_addition_request_format2(self):
        response = self.app.post('/math/matrix-addition', json={"data": {"foo": "bar"}})
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }')

    def test_matrix_addition_request_format3(self):
        response = self.app.post('/math/matrix-addition', json={"data": {}})
        self.assertEqual(response.json['meta']['error'], 'Matrix Addition requires atleast 2 operands')

    def test_matrix_addition_operand_format1(self):
        response = self.app.post('/math/matrix-addition', json={"data": {
            "param1": "foo",
            "param2": "bar"
        }})
        self.assertEqual(response.json['meta']['error'],
                         'Operands should be a matrix i.e list of lists of integers/floats')

    def test_matrix_addition_operand_format2(self):
        response = self.app.post('/math/matrix-addition', json={"data": {
            "param1": ["foo"],
            "param2": ["bar"]
        }})
        self.assertEqual(response.json['meta']['error'],
                         'Operands should be a matrix i.e list of lists of integers/floats')

    def test_matrix_addition_operand_format3(self):
        response = self.app.post('/math/matrix-addition', json={"data": {
            "param1": [["foo"]],
            "param2": [["bar"]]
        }})
        self.assertEqual(response.json['meta']['error'],
                         'Operands should be a matrix i.e list of lists of integers/floats')

    def test_matrix_addition_operand_format4(self):
        response = self.app.post('/math/matrix-addition', json={"data": {
            "param1": [[1], [2], [3]],
            "param2": [[1, 2, 3]]
        }})
        self.assertEqual(response.json['meta']['error'], 'Operands of matrix addition should be of same dimensions nxm')

    def test_matrix_addition_correctness(self):
        response = self.app.post('/math/matrix-addition', json={"data": {
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


if __name__ == '__main__':
    unittest.main()
