# api/models/comment.py
from django.db import models
from .post import Post

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.name
