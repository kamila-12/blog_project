from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length = 255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

def __str__(self):
    return self.title 
    

