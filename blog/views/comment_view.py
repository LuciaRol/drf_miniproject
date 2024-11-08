# blog/views/comment_view.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models.comment import Comment
from ..serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """ ViewSet for Comment model """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

