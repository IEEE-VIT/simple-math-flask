import sys,os,json,random
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
            checked if the sum of ints and the response is equal
        '''

        ints = [random.randint(0,100) for i in range(random.randint(0,20))]
        
        add_test = self.app.get('/math/add', data = json.dumps(str(ints)) , content_type='application/json') # dumps() did not accept list, so converted it to a string
        self.assertEqual(sum(ints), int(add_test.data)) # Response data is a string, so converted it to int

if __name__ == '__main__':
    unittest.main()