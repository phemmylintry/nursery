from rest_framework.test import APITestCase
from django.urls import reverse
from .models import CustomUser
from rest_framework import status

# Create your tests here.

class AccountsTest(APITestCase):

    def setUp(self):
        self.test_user = CustomUser.objects.create_user('test@test.com', 'pass1234', role='1')
        self.create_url = reverse('signup')
    

    def test_create_user(self):
        
        data = {
            "email" : "test@test2.com",
            "password" : "pass1234",
            "role" : "2"
        }

        response = self.client.post(self.create_url, data, format='json')
        #make sure two users are in the database
        self.assertEqual(CustomUser.objects.count(), 2)
        #Return status code 201 created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], response.data['email'])
        self.assertFalse('password' in response.data)

