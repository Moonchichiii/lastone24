from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

# Create your tests here.


class UserLoginTestCase(APITestCase):
    def test_user_login(self):
        user_data = {
            "username": "tester",
            "email": "testuser@gmail.com",
            "password": "buster2024"
        }
        user = User.objects.create_user(**user_data)

        login_data = {
            "username": user_data["username"],
            "password": user_data["password"]
        }
        client = APIClient()
        response = client.post(reverse('token_obtain_pair'), login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.data)
