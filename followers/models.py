from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Follower(models.Model):
    """
    Follower model, related to 'creator' and 'followed'.
    'creator' is a User that is following another User.
    'followed' is a User that is followed by 'creator'.
    We need the related_name attribute so that Django can differentiate
    between 'creator' and 'followed' who both are User model instances.
    'unique_together' ensures a user can't 'double follow' the same user.
    """
    creator = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['creator', 'followed']

    def __str__(self):
        return f'{self.creator} {self.followed}'
