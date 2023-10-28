import os
import sys
import unittest

sys.path.append(os.getcwd())

from app import app


class TestAddMatrix(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_matrix_multiplication_request_format1(self):
        """
        Test if '/math/matrix-multiplication' request contains data in json format
        """
        response = self.app.post('/math/matrix-multiplication')

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { '
                                                         'matrices: [matrix_1, matrix_2, ..., matrix_n] } Here matrix_1'
                                                         ', matrix_2, ..., matrix_n must be list of lists')

    def test_matrix_multiplication_request_format2(self):
        """
        Test if '/math/matrix-multiplication' request contains the correct format for key matrices
        """
        response = self.app.post('/math/matrix-multiplication', json={"matrices": {"foo": "bar"}})

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { '
                                                         'matrices: [matrix_1, matrix_2, ..., matrix_n] } Here matrix_1'
                                                         ', matrix_2, ..., matrix_n must be list of lists')

    def test_matrix_multiplication_request_format3(self):
        """
        Test '/math/matrix-multiplication' request body should contain at least two operands in matrices
        """
        response = self.app.post('/math/matrix-multiplication', json={"matrices": []})

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'], 'At least two matrices are required for multiplication')

    def test_matrix_multiplication_operand_format1(self):
        """
        Test '/math/matrix-multiplication' for a matrix should be a list of lists and can't be empty
        """
        response = self.app.post('/math/matrix-multiplication', json={
            "matrices": [
                [],
                "foo"
            ]})

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'], "A matrix can't be empty or a matrix should be a list "
                                                         "of lists of integers/floats")

    def test_matrix_multiplication_operand_format2(self):
        """
        Test '/math/matrix-multiplication' for a matrix should be a list of lists and a matrix row can't be empty
        """
        response = self.app.post('/math/matrix-multiplication', json={
            "matrices": [
                [[1, 3], []],
                [[1, 2], [2, 4]]
            ]
        })

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'], "A matrix row can't be Empty or A matrix row should be a list")

    def test_matrix_multiplication_operand_format3(self):
        """
        Test '/math/matrix-multiplication' for a matrix row should contain either an int or float
        """
        response = self.app.post('/math/matrix-multiplication', json={
            "matrices": [
                [[1, 3], ["a"]],
                [[1, 2], [2, 4]]
            ]
        })

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'], "A matrix row should contain either an int or float")

    def test_matrix_multiplication_operand_format4(self):
        """
        Test '/math/matrix-multiplication' for matrix dimensions for multiplications
        """
        response = self.app.post('/math/matrix-multiplication', json={
            "matrices": [
                [[1, 3]],
                [[1, 2]]
            ]
        })

        # assert statements
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.json['meta']['error'], "Matrix dimensions are not compatible for "
                                                         "multiplication! i.e. The columns of first matrix should"
                                                         " be equal to the rows of 2nd matrix and so on.")

    def test_matrix_multiplication_correctness(self):
        """
        Test '/math/matrix-multiplication' for correct output
        """
        response = self.app.post('/math/matrix-multiplication', json={
            "matrices": [
                [[1, 3]],
                [[1, 2], [3, 4]],
                [[6, 5], [4, 3]]
            ]
        })
        expected_result = [[116, 92]]

        # assert statements
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json['result'], expected_result)


if __name__ == '__main__':
    unittest.main()
