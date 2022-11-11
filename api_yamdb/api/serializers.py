from rest_framework.exceptions import ValidationError
from rest_framework.fields import CurrentUserDefault
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import (ModelSerializer, IntegerField)

from reviews.models import Genre, Category, Title, Review, Comment
from users.models import User
from api.validators import username_me, UsernameRegexValidator
from django.conf import settings


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
    rating = IntegerField(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        fields = ('id', 'name', 'year', 'rating', 'description', 'genre',
                  'category')
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


class ReviewSerializer(ModelSerializer):
    '''title = SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    '''

    author = SlugRelatedField(
        default=CurrentUserDefault(),
        slug_field='username',
        read_only=True
    )

    def validate(self, data):
        request = self.context['request']
        if request.method == 'POST':
            author = request.user
            title_id = self.context['view'].kwargs.get('title_id')
            title = get_object_or_404(Title, pk=title_id)
            if Review.objects.filter(title=title, author=author).exists():
                raise ValidationError(
                    'Нельзя добавить больше 1 комментария'
                )
        return data

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date', 'title')
        model = Review
        read_only_fields = ('title',)


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment
        read_only_fields = ('review',)


class UserSerializer(ModelSerializer):

    class Meta:
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        model = User

    def validate_username(self, value):
        return username_me(value)


class UserEditSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        read_only_fields = ('role',)


class SignupSerializer(serializers.Serializer):
    username_validator = UsernameRegexValidator()
    username = serializers.CharField(
        max_length=settings.LIMIT_USERNAME,
        required=True,
        validators=[username_validator, username_me],
        error_messages={
            'unique': 'Пользователь с таким именем уже существует!',
        },
    )
    email = serializers.EmailField(
        max_length=settings.LIMIT_EMAIL,
        required=True
    )


class TokenSerializer(serializers.Serializer):
    username_validator = UsernameRegexValidator()
    username = serializers.CharField(
        max_length=settings.LIMIT_USERNAME,
        required=True,
        validators=[username_validator, username_me],
        error_messages={
            'unique': 'Пользователь с таким именем уже существует!',
        },
    )
    confirmation_code = serializers.CharField(
        max_length=settings.LIMIT_CODE,
        required=True
    )

    def validate_username(self, value):
        return username_me(value)
