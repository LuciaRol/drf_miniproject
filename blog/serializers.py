""" Serializers for the blog app """
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    """ Serializer for the Comment model """
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), required=False)
    email = serializers.ReadOnlyField(source='user.email')
    name = serializers.CharField(max_length=255)
    body = serializers.CharField(max_length=2000)

    class Meta:
        """ Meta class for the CommentSerializer """
        model = Comment
        fields = ['id', 'post', 'name', 'email', 'body', 'created_at']
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        user = self.context['request'].user  # Obtener el usuario autenticado
        validated_data['user'] = user
        return super().create(validated_data)





class PostSerializer(serializers.ModelSerializer):
    """ Serializer for the Post model """
    comments = CommentSerializer(many=True, required=False)
    user_id = serializers.ReadOnlyField(source='author.id')
    username = serializers.ReadOnlyField(source='author.username')
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        """ Meta class for the PostSerializer """
        model = Post
        fields = ['id', 'user_id', 'username', 'title', 'body', 'comments', 'comments_count', 'created_at']
        read_only_fields = ['id', 'user_id', 'username']

    def create(self, validated_data):
        comments_data = validated_data.pop('comments', [])

        # Asignar el usuario actual o el predeterminado (99999942)
        user = self.context['request'].user if 'request' in self.context else User.objects.get(id=99999942)
        validated_data['author'] = user

        # Crear el post
        post = Post.objects.create(**validated_data)

        # Si se proporcionan comentarios, crear los comentarios
        for comment_data in comments_data:
            comment_data['post'] = post
            comment_data['user'] = comment_data.get('user', user)
            Comment.objects.create(**comment_data)

        return post



class UserSerializer(serializers.ModelSerializer):
    """ Serializer for the User model """
    password = serializers.CharField(write_only=True)

    class Meta:
        """ Meta class for the UserSerializer """
        model = User
        fields = ['id', 'email', 'username', 'password']

    def create(self, validated_data):
        # Hash the password before saving the user
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        # If a new password is provided, hash it before saving
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).update(instance, validated_data)
