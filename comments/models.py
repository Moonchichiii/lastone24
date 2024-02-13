from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


# Create your models here.

class Comment(models.Model):
    """
    Comment model, related to User and Post
    """
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_created')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
