from cadUsuarios.api.serializers import UsuarioSerializer
from cadUsuarios.exceptions import PythonDjangoException
from cadUsuarios.models import Phone, User
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (IsAuthenticated, )
    def create(self, request):
        serializer = UsuarioSerializer(data=request.data)
        response = Response()
        if serializer.is_valid():
            phones = request.data.pop('phones')
            data_user = request.data
            user = User.objects.create_user(**data_user)
            for phone in phones:
                p = Phone(number=phone['number'], area_code=phone['area_code'], country_code=phone['country_code'],
                          user=user)
                p.save()
            return Response(data=response.data, status=status.HTTP_201_CREATED)
        else:
            raise PythonDjangoException(message=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
