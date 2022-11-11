from datetime import datetime

from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from users.models import User


class CategoryGenreModel(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.slug

    class Meta:
        abstract = True
        ordering = ('name',)


class Title(models.Model):
    name = models.CharField(max_length=256)
    year = models.PositiveSmallIntegerField(db_index=True, validators=[
        MinValueValidator(1730), MaxValueValidator(datetime.now().year)])
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField('Genre', blank=True, related_name='titles')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
                                 null=True, blank=True, related_name='titles')

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('name',)

    def __str__(self):
        return self.name[:settings.OUTPUT_LENGTH]


class Category(CategoryGenreModel):
    class Meta(CategoryGenreModel.Meta):
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(CategoryGenreModel):

    class Meta(CategoryGenreModel.Meta):
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class ReviewCommentModel(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True,
    )

    class Meta:
        abstract = True
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:settings.OUTPUT_LENGTH]

class Review(ReviewCommentModel):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE
    )
    score = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    class Meta(ReviewCommentModel.Meta):
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        default_related_name = 'reviews'
        constraints = [
            models.UniqueConstraint(
                fields=('title', 'author'),
                name='unique_review'
            ),
        ]


class Comment(ReviewCommentModel):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE
    )

    class Meta(ReviewCommentModel.Meta):
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        default_related_name = 'comments'
