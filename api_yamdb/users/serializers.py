from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (EmailField, CharField,
                                        ModelSerializer, Serializer)
from rest_framework.validators import UniqueValidator

from users.models import User


class UserSerializer(ModelSerializer):
    username = CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ],
        required=True,
    )
    email = EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    class Meta:
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        model = User


class UserEditSerializer(ModelSerializer):
    class Meta:
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        model = User
        read_only_fields = ('role',)


class SignupSerializer(ModelSerializer):
    username = CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    email = EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    def validate_username(self, value):
        if value.lower() == 'me':
            raise ValidationError("Нельзя 'me'!!!")
        return value

    class Meta:
        fields = ("username", "email")
        model = User


class TokenSerializer(Serializer):
    username = CharField()
    confirmation_code = CharField()
