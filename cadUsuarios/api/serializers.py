from cadUsuarios.models import Phone, User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = (
                    'number',
                    'area_code',
                    'country_code',
                )

class UsuarioSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer( many=True, read_only=True)
    class Meta:
        model = User
        fields = (  
                    'first_name',
                    'last_name',
                    'email', 
                    'password',
                    'phones',
                )
        depth = 1


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['email'] = user.email
        return token
        
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ( 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True}
        }


    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            password=validated_data['password']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user