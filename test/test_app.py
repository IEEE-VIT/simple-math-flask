import sys,os
sys.path.append(os.getcwd())

from app import app
import os 
import unittest

class AppTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_check(self):
        response = self.app.get('/math/check')
        self.assertEqual(response.data, b'Congratulations! Your app works. :)')

    #Add the test_cases for various functionality here

    def test_division_request_format1(self):
        response = self.app.post('/math/division')
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }')
    
    def test_division_request_format2(self):
        response = self.app.post('/math/division', json={ "data": { "foo": "bar" } })
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }')

    def test_division_request_format3(self):
        response = self.app.post('/math/division', json={ "data": {"param1":1} })
        self.assertEqual(response.json['meta']['error'], 'Division requires exactly 2 operands')
    
    def test_division_request_format4(self):
        response = self.app.post('/math/division', json={ "data": {"param1":1, "param2":2, "param3":3} })
        self.assertEqual(response.json['meta']['error'], 'Division requires exactly 2 operands')
    
    def test_division_operand_format1(self):
        response = self.app.post('/math/division', json={ "data": {
            "param1": "foo",
            "param2": "bar"
        } })
        self.assertEqual(response.json['meta']['error'], 'Operands should be a real number i.e. integer/float')
    
    def test_division_operand_format2(self):
        response = self.app.post('/math/division', json={ "data": {
            "param1": 1,
            "param2": 0
        } })
        self.assertEqual(response.json['meta']['error'], 'Division by zero is not allowed')
    
    def test_division_correctness(self):
        response = self.app.post('/math/division', json={ "data": {
            "param1": 3,
            "param2": 2,
        } })
        self.assertEqual(response.json['result'], 1.5)

    def test_exponentiation_request_format1(self):
        response = self.app.post('/math/exponentiation')
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { data: { param1: <value>, param2: <value> } }')
    
    def test_exponentiation_request_format2(self):
        response = self.app.post('/math/exponentiation', json={ "data": { "foo": "bar" } })
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { data: { param1: <value>, param2: <value> } }')

    def test_exponentiation_request_format3(self):
        response = self.app.post('/math/exponentiation', json={ "data": {} })
        self.assertEqual(response.json['meta']['error'], 'The request must contain exactly two operands.')

    def test_exponentiation_operand_format(self):
        response = self.app.post('/math/matrixaddition', json={ "data": {
            "param1": "foo",
            "param2": "bar"
        } })
        self.assertEqual(response.json['meta']['error'], 'Operands must be integers/floats.')

    def test_exponentiation_correctness(self):
        response = self.app.post('/math/matrixaddition', json={ "data": {
            "param1": 5,
            "param2": 3
        } })
        self.assertEqual(response.json['result'], 125)
    
    def test_matrix_addition_request_format1(self):
        response = self.app.post('/math/matrixaddition')
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }')

    def test_matrix_addition_request_format2(self):
        response = self.app.post('/math/matrixaddition', json={ "data": { "foo": "bar" } })
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }')

    def test_matrix_addition_request_format3(self):
        response = self.app.post('/math/matrixaddition', json={ "data": {} })
        self.assertEqual(response.json['meta']['error'], 'Matrix Addition requires atleast 2 operands')

    def test_matrix_addition_operand_format1(self):
        response = self.app.post('/math/matrixaddition', json={ "data": {
            "param1": "foo",
            "param2": "bar"
        } })
        self.assertEqual(response.json['meta']['error'], 'Operands should be a matrix i.e list of lists of integers/floats')
    
    def test_matrix_addition_operand_format2(self):
        response = self.app.post('/math/matrixaddition', json={ "data": {
            "param1": ["foo"],
            "param2": ["bar"]
        } })
        self.assertEqual(response.json['meta']['error'], 'Operands should be a matrix i.e list of lists of integers/floats')
    
    def test_matrix_addition_operand_format3(self):
        response = self.app.post('/math/matrixaddition', json={ "data": {
            "param1": [["foo"]],
            "param2": [["bar"]]
        } })
        self.assertEqual(response.json['meta']['error'], 'Operands should be a matrix i.e list of lists of integers/floats')
    
    def test_matrix_addition_operand_format4(self):
        response = self.app.post('/math/matrixaddition', json={ "data": {
            "param1": [[1], [2], [3]],
            "param2": [[1, 2, 3]]
        } })
        self.assertEqual(response.json['meta']['error'], 'Operands of matrix addition should be of same dimensions nxm')
    
    def test_matrix_addition_correctness(self):
        response = self.app.post('/math/matrixaddition', json={ "data": {
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
        } })
        self.assertEqual(response.json['result'], [
            [6, 6],
            [6, 6]
        ])

if __name__ == '__main__':
    unittest.main()
