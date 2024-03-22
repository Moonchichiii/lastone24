from django.db import models
from profiles.models import Profile

# Create your models here.
class Post(models.Model):
    """
    Post model 
    """    
    
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    ingredients = models.TextField(blank=True, null=True)
    recipe = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=False)
    image_url = models.URLField(blank=True, null=True)  
    published = models.BooleanField(default=False)
    time = models.IntegerField(default=0)  

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'