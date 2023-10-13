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

    def test_matrix_addition_request_format1(self):
        response = self.app.post('/math/matrixaddition')
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }')
    
    def test_matrix_addition_request_format1(self):
        response = self.app.post('/math/matrixaddition', json={ "data": { "foo": "bar" } })
        self.assertEqual(response.json['meta']['error'], 'The request must be a JSON of the following format: { data: { param1: <value>, ... param<n>: <value> } }')

    def test_matrix_addition_request_format3(self):
        response = self.app.post('/math/matrixaddition', json={ "data": {} })
        self.assertEqual(response.json['meta']['error'], 'Matrix Addition requires atleast 2 operands')

if __name__ == '__main__':
    unittest.main()