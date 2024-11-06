# api/models/post.py
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True)


    def __str__(self):
        return self.title
