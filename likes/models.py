
from django.db import models
from profiles.models import Profile
from posts.models import Post



# Create your models here.

class Like(models.Model):
    """
    Like model, related to 'creator' and 'post'.
    'creator' is a User instance and 'post' is a Post instance.
    'unique_together' ensures a user can't like the same post twice.
    """
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='likes_created')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['creator', 'post']

    def __str__(self):
        return f'{self.creator} likes {self.post}'
