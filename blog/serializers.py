# api/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post
from .models import Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'comments'] 


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


