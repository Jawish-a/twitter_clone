from django.db import models
from django.contrib.auth.models import User

#####################################################################################################
#       Profile Model                                                                               #
#####################################################################################################

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=191)
    is_active = models.BooleanField(default=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True) 
    city = models.CharField(max_length=191)

    def __str__(self):
        return self.user


#####################################################################################################
#       Post Model                                                                                  #
#####################################################################################################
class Post(models.Model):
    content = models.CharField(max_length=191)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)
    auther = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    
    def __str__(self):
        return self.content

#####################################################################################################
#       Image Model                                                                                 #
#####################################################################################################

# class Image(models.Model):
#     post = models.ManyToManyField(Post, related_name="images" , related_query_name="posts" )

#####################################################################################################
#       Channel Model                                                                               #
#####################################################################################################

class Subejct(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.user

