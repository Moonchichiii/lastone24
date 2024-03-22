from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Profile(models.Model):
    creator = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    image = models.ImageField(
    upload_to='media/', default='7190932_mcpghm'
)

    
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.creator.username}'s profile"
