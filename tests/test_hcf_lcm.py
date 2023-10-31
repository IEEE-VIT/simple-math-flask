import os
import sys
import unittest

sys.path.append(os.getcwd())

from app import app


class TestHcfLcm(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_test_hcf_lcm_format1(self):
        """
        Test if '/math/hcf-lcm' request contains the correct keys in data
        """
        response = self.app.post('/math/hcf-lcm')

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { a: <value>, b: <value>} }')

    def test_test_hcf_lcm_format2(self):
        """
        Test if '/math/hcf-lcm' request contains the correct keys in data
        """
        response = self.app.post('/math/hcf-lcm', json={"data": {"foo": "bar"}})

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'],
                         'The request must be a JSON of the following format: { data: { a: <value>, b: <value>} }')

    def test_hcf_lcm_operand_format(self):
        """
        Test if '/math/hcf-lcm' request data keys are of correct format
        """
        response = self.app.post('/math/hcf-lcm', json={"data": {
            "a": "2",
            "b": 9.7
        }})

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'],
                         'Operands a, b should be either an int Only')

    def test_hcf_lcm_correctness1(self):
        """
        Test if '/math/hcf-lcm' request for correct output
        """
        response = self.app.post('/math/hcf-lcm', json={"data": {
            "a": 13,
            "b": 23
        }})

        # assert statements
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json['result'], {'hcf': 1, 'lcm': 299})
        self.assertEqual(response.json['meta'], {})

    def test_hcf_lcm_correctness2(self):
        """
        Test if '/math/hcf-lcm' request for correct output
        """
        response = self.app.post('/math/hcf-lcm', json={"data": {
            "a": 20,
            "b": -8
        }})

        # assert statements
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json['result'], {"hcf": 4, "lcm": 40})
        self.assertEqual(response.json['meta'], {})

    def test_hcf_lcm_correctness3(self):
        """
        Test if '/math/hcf-lcm' request for correct output
        """
        response = self.app.post('/math/hcf-lcm', json={"data": {
            "a": -6,
            "b": -8
        }})

        # assert statements
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json['result'], {"hcf": 2, "lcm": 24})
        self.assertEqual(response.json['meta'], {})


if __name__ == '__main__':
    unittest.main()
