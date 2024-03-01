from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from profiles.models import Profile
from posts.models import Post
from comments.models import Comment

# Create your tests here.


class CommentCreateTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tester2024", password="buster")
        self.profile, _ = Profile.objects.get_or_create(creator=self.user)
        self.post = Post.objects.create(
            creator=self.profile, title="testing post!!")

    def test_comment_post(self):
        self.client.force_authenticate(user=self.user)
        data = {"content": "Good pie!", "post": self.post.id}
        response = self.client.post('/comments/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CommentDetailTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="tester2024", password="buster")
        self.profile, _ = Profile.objects.get_or_create(creator=self.user)
        self.post = Post.objects.create(
            creator=self.profile, title="test")
        self.comment = Comment.objects.create(
            creator=self.profile, post=self.post, content="look amazing!!!")

    def test_comment_detail(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'/comments/{self.comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



