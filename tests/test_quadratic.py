import os
import sys
import unittest

sys.path.append(os.getcwd())

from app import app


class TestAddMatrix(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_quadratic_request_format1(self):
        """
        Test if '/math/quadratic-equation' request contains data in json format
        """
        response = self.app.post('/math/quadratic-equation')

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { a: <value>, b: <value>, '
                         'c: <value>} }')

    def test_quadratic_request_format2(self):
        """
        Test if '/math/quadratic-equation' request contains the correct keys in data
        """
        response = self.app.post('/math/quadratic-equation', json={"data": {"foo": "bar"}})

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { a: <value>, b: <value>, '
                         'c: <value>} }')

    def test_quadratic_operand_format(self):
        """
        Test if '/math/quadratic-equation' request data keys are of correct format
        """
        response = self.app.post('/math/quadratic-equation', json={"data": {
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
        Test if '/math/quadratic-equation' request for correct output
        """
        response = self.app.post('/math/quadratic-equation', json={"data": {
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
