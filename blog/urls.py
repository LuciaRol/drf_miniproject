# api/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularSwaggerView, 
    SpectacularRedocView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserViewSet, PostViewSet, CommentViewSet, RegisterView


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    path('api/login/', TokenObtainPairView.as_view(), name='login'), # Es lo mismo que el api/token/ ?
    path('api/register/', RegisterView.as_view(), name='register'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),  # Ruta para el esquema OpenAPI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Ruta para Swagger UI
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc-ui'),  # Ruta para ReDoc UI
]
