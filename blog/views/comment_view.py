# blog/views/comment_view.py
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from ..models.comment import Comment
from ..serializers import CommentSerializer

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user  # Verifica si el comentario pertenece al usuario

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        user = self.request.user

        # Verificar si el usuario está autenticado
        if user.is_authenticated:
            serializer.save(user=user)  # Asignar el usuario autenticado al comentario
        else:
            raise PermissionDenied("You must be logged in to create a comment.")
