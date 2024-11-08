"""Este archivo se encarga de definir las rutas de la API REST."""
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
from .views import (
    UserViewSet, 
    PostViewSet, 
    CommentViewSet, 
    RegisterViewSet
)


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'register', RegisterViewSet, basename='register')

urlpatterns = [
    path('', include(router.urls)),
    
    path(
        'api/login/', 
        TokenObtainPairView.as_view(), 
        name='login'
    ),
    # path('register/', RegisterViewSet.as_view({'post': 'create'}), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),  # Ruta para el esquema OpenAPI
    path(
        'swagger/', 
        SpectacularSwaggerView.as_view(url_name='schema'), 
        name='swagger-ui'
    ),  # Ruta para Swagger UI
    path(
        'redoc/', 
        SpectacularRedocView.as_view(url_name='schema'), 
        name='redoc-ui'
    ),  # Ruta para ReDoc UI
]
