from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), required=False)  # No es obligatorio enviar el 'post'

    class Meta:
        model = Comment
        fields = ['id', 'post', 'name', 'email', 'body']
        read_only_fields = ['id', 'user'] 

    def validate_post(self, value):
        if not value.published:
            raise serializers.ValidationError("No se pueden agregar comentarios a un post que no está publicado.")
        return value


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'user_id', 'title', 'body', 'comments']
        read_only_fields = ['id', 'user_id']

    def create(self, validated_data):
        comments_data = validated_data.pop('comments', [])

        # Asignar el usuario actual o el predeterminado (99999942)
        user = self.context['request'].user if 'request' in self.context else User.objects.get(id=99999942)
        validated_data['user_id'] = user.id

        # Crear el post
        post = Post.objects.create(**validated_data)

        # Si se proporcionan comentarios, crear los comentarios
        for comment_data in comments_data:
            comment_data['post'] = post
            comment_data['user'] = comment_data.get('user', user)
            Comment.objects.create(**comment_data)

        return post




class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
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
