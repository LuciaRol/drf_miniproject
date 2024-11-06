# blog/views/post_view.py
from rest_framework import viewsets, permissions
from ..models.post import Post
from ..serializers import PostSerializer

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, views, obj):
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(user_id=99999942)  # Asignar user_id fijo


