from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Post(models.Model):
    creator = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    content = models.CharField(max_length=500,default="")
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField(default=0)