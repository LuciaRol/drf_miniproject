# api/serializers.py
from rest_framework import serializers
from .models.post import Post
from .models.comment import Comment

class PostSerializer(serializers.ModelSerializer):
    # Incluye los comentarios relacionados en el mismo serializador de Post
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user_id', 'title', 'body', 'comments']
        read_only_fields = ['id', 'user_id']  # Los campos 'id' y 'user_id' son de solo lectura


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'name', 'email', 'body']
        read_only_fields = ['id']  # 'id' es de solo lectura