from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from profiles.models import Profile

# Create your tests here.

class ProfileDetailTestCase(APITestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username="tester", password="buster2024")
        
        self.profile = Profile.objects.get(creator=self.user)

    def test_profile_detail(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('profile-detail', kwargs={'pk': self.profile.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)