import sys,os,json,random
from flask import jsonify
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
        
        '''
        Test for add-function:
            Initialised a random array ints and sent a request to the add-function route, and finally
            checked if the sum of ints and the response is equal. Also checked if the wrong requests are
            properly detected.
        '''

        ints = [random.randint(0,100) for i in range(random.randint(0,20))]
        
        add_test_1 = self.app.post('/math/add', data = json.dumps(str(ints)) , content_type='application/json') # dumps() did not accept list, so converted it to a string
        self.assertEqual(sum(ints), int(add_test_1.data)) # Response data is a string, so converted it to int
        add_test_2 = self.app.post('/math/add') 
        self.assertEqual(b'No input was given',add_test_2.data)
        add_test_3 = self.app.post('/math/add', json = json.dumps('random string') , headers = {'Content-Type': 'application/json'})
        self.assertEqual(b'random string is not a valid input',add_test_3.data)
        
if __name__ == '__main__':
    unittest.main()