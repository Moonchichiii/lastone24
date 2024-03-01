from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from profiles.models import Profile
from posts.models import Post
from likes.models import Like

# Create your tests here.


class LikeCreateTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tester2024", password="buster")

        if hasattr(self.user, 'profile'):
            self.profile = self.user.profile
        else:
            self.profile = Profile.objects.create(creator=self.user)
        self.post = Post.objects.create(
            creator=self.profile, title="testing post")

    def test_like_post(self):
        self.client.force_authenticate(user=self.profile.creator)
        response = self.client.post('/likes/', {'post': self.post.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UnlikePostTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tester2024", password="buster")

        if hasattr(self.user, 'profile'):
            self.profile = self.user.profile
        else:
            self.profile = Profile.objects.create(creator=self.user)
        self.post = Post.objects.create(
            creator=self.profile, title="testing post")
        self.like = Like.objects.create(creator=self.profile, post=self.post)

    def test_unlike_post(self):
        self.client.force_authenticate(user=self.profile.creator)
        response = self.client.delete(f'/likes/{self.like.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
