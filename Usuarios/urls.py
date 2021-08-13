from cadUsuarios.api.routers import router as usuarios_router
from cadUsuarios.views import MyObtainTokenPairView, RegisterView
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from cadUsuarios import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('me/', views.me),
    path('signin/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('', include(usuarios_router.urls)),
]
