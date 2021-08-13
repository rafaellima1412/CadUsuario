from cadUsuarios.api.viewsets import PostViewSet
from rest_framework.routers import  DefaultRouter

router = DefaultRouter()

router.register('signup', PostViewSet, basename='Usuarios')

