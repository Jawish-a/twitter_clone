from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=191)
    created_at = models.DateTimeField(auto_now=True)
    img = models.ImageField(null=True, blank=True)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content