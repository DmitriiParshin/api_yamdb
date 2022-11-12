from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CurrentUserDefault, CharField, EmailField
from rest_framework.serializers import (ModelSerializer, IntegerField,
                                        Serializer)
from rest_framework.generics import get_object_or_404
from rest_framework.relations import SlugRelatedField

from reviews.models import (Genre, Category, Title, Review, Comment,
                            get_year_now)
from users.models import User
from api.validators import username_me, UsernameValidator


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
    year = IntegerField(
        validators=[MinValueValidator(1730),
                    MaxValueValidator(get_year_now())]
    )
    genre = SlugRelatedField(
        slug_field='slug', many=True, queryset=Genre.objects.all()
    )
    category = SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all()
    )

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')
        model = Title

    def to_representation(self, value):
        serializer = TitleReadSerializer(value)
        return serializer.data


class ReviewSerializer(ModelSerializer):
    author = SlugRelatedField(
        default=CurrentUserDefault(),
        slug_field='username',
        read_only=True
    )
    score = IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
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


class SignupSerializer(Serializer):
    username = CharField(
        max_length=settings.LIMIT_USERNAME,
        required=True,
        validators=[UsernameValidator(), username_me],
    )
    email = EmailField(
        max_length=settings.LIMIT_EMAIL,
        required=True
    )


class TokenSerializer(Serializer):
    username = CharField(
        max_length=settings.LIMIT_USERNAME,
        required=True,
        validators=[UsernameValidator(), username_me],
    )
    confirmation_code = CharField(
        max_length=settings.LIMIT_CODE,
        required=True
    )

    def validate_username(self, value):
        return username_me(value)
