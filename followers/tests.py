from django.contrib.auth.models import User
from profiles.models import Profile
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from followers.models import Follower

# Create your tests here.


class FollowTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tester2024", password="buster")
        self.user_to_follow = User.objects.create_user(
            username="following", password="buster")

        self.profile, _ = Profile.objects.get_or_create(creator=self.user)
        self.profile_to_follow, _ = Profile.objects.get_or_create(
            creator=self.user_to_follow)



    def test_follow(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            '/followers/', {'followed': self.profile_to_follow.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)




class UnfollowTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tester2024", password="buster")
        self.user_to_unfollow = User.objects.create_user(
            username="unfolloweduser", password="password123")
        self.profile, _ = Profile.objects.get_or_create(creator=self.user)
        self.profile_to_unfollow, _ = Profile.objects.get_or_create(
            creator=self.user_to_unfollow)
        self.follow = Follower.objects.create(
            creator=self.profile, followed=self.profile_to_unfollow)


    def test_unfollow(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/followers/{self.follow.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
