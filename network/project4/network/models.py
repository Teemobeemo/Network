from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.views.debug import default_urlconf


class UserProfile(AbstractUser):
    bio = models.CharField(max_length=1000)

class Post(models.Model):
    creator = models.ForeignKey(UserProfile,default=1,on_delete=models.CASCADE)
    content = models.CharField(max_length=500,default="")
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField(default=0)

class Follow(models.Model):
    user_id  = models.ForeignKey(UserProfile,default=1,on_delete=models.CASCADE,related_name='user')
    follow_id = models.ForeignKey(UserProfile,default=2,on_delete=models.CASCADE,related_name='followed')

class Like(models.Model):
    user = models.ForeignKey(UserProfile,default=1,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,default=1)