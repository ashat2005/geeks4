from django.test import TestCase,Client
from django.urls import reverse
# Create your tests here.
class HelloViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_index(self):
        response = self.client.get(reverse("index-page"))
        self.assertTemplateNotUsed(response,"blog/index.html")
        self.assertEqual(200, response.status_code)

    def test_about(self):
        response = self.client.get(reverse("about-view"))
        self.assertTemplateNotUsed(response,"blog/about.html")    
        self.assertEqual(200, response.status_code)
    
    def test_contacts(self):
        response = self.client.get(reverse("contacts-view"))
        self.assertTemplateNotUsed(response,"blog/contacts.html")
        self.assertContains(response, "number")
        self.assertEqual(200, response.status_code)

    # def test_about(self):
    #     response = self.client.get(reverse("about-view"))
    #     self.assertContains(response, "about")
    #     self.assertEqual(200, response.status_code)
    # def test_hello(self):
    #     response = self.client.get(reverse("hello-view"))
    #     expected_data = "Hello"
    #     self.assertEqual(expected_data, response.content.decode())
    #     self.assertEqual(500, response.status_code)
    #     self.assertEqual(response['name'], 'alex')        
    # def test_contacts(self):
    #     response = self.client.get(reverse("contacts-view"))
    #     expected_data = "number"
    #     self.assertEqual(expected_data, response.content.decode())

    # def test_about(self):
    #     response = self.client.get(reverse("about-view"))
    #     expected_data = "about"
    #     self.assertEqual(expected_data, response.content.decode())