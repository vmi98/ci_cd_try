import unittest
from main import app 

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_framework(self):
        response = self.client.get('/platform')
        self.assertEqual(response.status_code, 200)
    
    def test_platform(self):
        response = self.client.get('/framework')
        self.assertEqual(response.status_code, 200)      

if __name__ == '__main__':
    unittest.main()
