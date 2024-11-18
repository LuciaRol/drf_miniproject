# views.py en tu app de Django

from rest_framework_simplejwt.views import TokenObtainPairView

# Agrega una vista para obtener el token cuando el usuario se autentique
class CustomTokenObtainPairView(TokenObtainPairView):
    """ Custom TokenObtainPairView """
    pass
