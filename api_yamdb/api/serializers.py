from rest_framework.serializers import (ModelSerializer, Serializer,
                                        SlugRelatedField)

from api.models import Genre, Category, Title
from users.models import User

from rest_framework import serializers


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id',)
        lookup_field = 'slug'


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        exclude = ('id',)
        lookup_field = 'slug'


class TitleReadSerializer(ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')
        model = Title


class TitleWriteSerializer(ModelSerializer):
    genre = SlugRelatedField(
        slug_field='slug', many=True, queryset=Genre.objects.all()
    )
    category = SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all()
    )

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')
        model = Title


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True,)

    class Meta:
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        model = User


class SignupSerializer(ModelSerializer):

    class Meta:
        fields = ('email', 'username')
        model = User


class TokenSerializer(Serializer):

    username = serializers.CharField(max_length=150)
    confirmation_code = serializers.CharField()
