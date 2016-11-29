from django.test import TestCase
from django.test import Client

# Create your tests here.

class ResponseTestAccount(TestCase):
    
    def setUp(self):
        print("Set up [ Response Test ] : account")
        self.client = Client()

    def test_index(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Response : http://localhost:port/")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")