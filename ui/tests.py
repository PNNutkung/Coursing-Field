from django.test import TestCase
from django.test import Client
from django.urls import reverse
# Create your tests here.

class ResponseTestUI(TestCase):

    def setUp(self):
        print("Set uo [ Response Test ] : UI")
        self.client = Client()

    def test_ui(self):
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         print("Response : http://localhost:port/ui")
         response = self.client.get('/ui')
         self.assertEqual(response.status_code, 301)
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def test_ui_view(self):
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         print("Response : http://localhost:port/ui/view")
         response = self.client.get('/ui/view')
         self.assertEqual(response.status_code, 200)
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def test_ui_browse(self):
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         print("Response : http://localhost:port/ui/browse")
         response = self.client.get('/ui/browse')
         self.assertEqual(response.status_code, 200)
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def test_ui_register(self):
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         print("Response : http://localhost:port/ui/register")
         response = self.client.get('/ui/register')
         self.assertEqual(response.status_code, 200)
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def test_ui_create(self):
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         print("Response : http://localhost:port/ui/create")
         response = self.client.get('/ui/create')
         self.assertEqual(response.status_code, 200)
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
    def test_ui_profile(self):
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         print("Response : http://localhost:port/ui/profile")
         response = self.client.get('/ui/profile')
         self.assertEqual(response.status_code, 200)
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")



