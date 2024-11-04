from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from ..serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    """ Endpoint """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'blog': reverse('blog-list', request=request, format=format)
    })
    