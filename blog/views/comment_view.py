# blog/views/comment_view.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from ..models.comment import Comment
from ..serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user

        # Verificar si el usuario está autenticado
        if user.is_authenticated:
            serializer.save(user=user)  # Asignar el usuario autenticado al comentario
        else:
            raise PermissionDenied("You must be logged in to create a comment.")
