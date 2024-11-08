""" User view module """
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from blog.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """ ViewSet for User model """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    