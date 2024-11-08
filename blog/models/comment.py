# blog/models/comment.py
from django.contrib.auth.models import User
from django.db import models
from .post import Post

class Comment(models.Model):
    """ Model for comments on blog posts """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.name
