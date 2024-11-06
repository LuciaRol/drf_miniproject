# blog/views/post_view.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models.post import Post
from ..serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=99999942)  # Asignar user_id fijo
