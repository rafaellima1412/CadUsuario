from rest_framework import generics
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from cadUsuarios.api.serializers import (MyTokenObtainPairSerializer,
                                         RegisterSerializer)
from cadUsuarios.exceptions import PythonDjangoException
from cadUsuarios.models import Phone, User


@api_view(['GET'])
@authentication_classes((JWTAuthentication,))
@permission_classes((IsAuthenticated,))
def me(request, **kwargs):
    try:
        data_user = request.user
        response = {
            'first_name': data_user.first_name,
            'last_name': data_user.last_name,
            'email': data_user.email,
            'last_login': data_user.last_login,
            'created_at': data_user.created_at,
            'phones': Phone.objects.values('number', 'area_code', 'country_code').filter(user_id=data_user.id),
        }
        return Response(data=response)
    except PythonDjangoException as e:
        return Response(e.detail, status=e.status_code)

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


