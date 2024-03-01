from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from posts.models import Post

# Create your tests here.


class PostAndLikeTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='tester2024', password='buster')
        self.client.force_authenticate(user=self.user)
        self.profile = self.user.profile
        self.post = Post.objects.create(
            title="PostAndLikeTest", recipe="good recipe", creator=self.user.profile)

    def test_create_post(self):
        post_count_before = Post.objects.count()
        data = {
            "title": "Pan seared fish",
            "recipe": "Mix ingredients thoroughly",
        }
        response = self.client.post('/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), post_count_before + 1)
        self.assertEqual(Post.objects.latest('id').title, data['title'])

    def test_like(self):
        like_data = {'post': self.post.id, 'creator': self.profile.id}
        response = self.client.post('/likes/', like_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
