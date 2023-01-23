from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api.validators import get_year_now
from users.models import User


class CategoryGenreModel(models.Model):
    name = models.CharField(
        "Название категории", max_length=settings.LIMIT_NAME
    )
    slug = models.SlugField(
        "Слаг категории", max_length=settings.LIMIT_SLUG, unique=True
    )

    class Meta:
        abstract = True
        ordering = ("name",)

    def __str__(self):
        return self.slug


class Title(models.Model):
    name = models.CharField(
        "Название произведения", max_length=settings.LIMIT_NAME
    )
    year = models.PositiveSmallIntegerField(
        "Год выпуска произведения",
        db_index=True,
        validators=[
            MinValueValidator(settings.MIN_YEAR),
            MaxValueValidator(get_year_now),
        ],
    )
    description = models.TextField(
        "Описание произведения", null=True, blank=True
    )
    genre = models.ManyToManyField(
        "Genre",
        verbose_name="Жанр произведения",
        blank=True,
        related_name="titles",
    )
    category = models.ForeignKey(
        "Category",
        verbose_name="Категория произведения",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="titles",
    )

    class Meta:
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"
        ordering = ("name",)

    def __str__(self):
        return self.name[: settings.OUTPUT_LENGTH]


class Category(CategoryGenreModel):
    class Meta(CategoryGenreModel.Meta):
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Genre(CategoryGenreModel):
    class Meta(CategoryGenreModel.Meta):
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class GenreTitle(models.Model):
    genre = models.ForeignKey(
        Genre, verbose_name="Жанр", on_delete=models.CASCADE
    )
    title = models.ForeignKey(
        Title, verbose_name="Произведениe", on_delete=models.CASCADE
    )


class ReviewCommentModel(models.Model):
    text = models.TextField("Текст")
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )
    pub_date = models.DateTimeField(
        "Дата добавления",
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        abstract = True
        ordering = ("-pub_date",)

    def __str__(self):
        return self.text[: settings.OUTPUT_LENGTH]


class Review(ReviewCommentModel):
    title = models.ForeignKey(
        Title, verbose_name="Произведение", on_delete=models.CASCADE
    )
    score = models.SmallIntegerField(
        "Оценка произведения",
        validators=[
            MinValueValidator(
                1, message="Оценка должна быть больше или равна 1"
            ),
            MaxValueValidator(
                10, message="Оценка должна быть меньше или равна 10"
            ),
        ],
        default=1,
    )

    class Meta(ReviewCommentModel.Meta):
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        default_related_name = "reviews"
        constraints = [
            models.UniqueConstraint(
                fields=("title", "author"), name="unique_review"
            ),
        ]


class Comment(ReviewCommentModel):
    review = models.ForeignKey(
        Review, verbose_name="Отзыв", on_delete=models.CASCADE
    )

    class Meta(ReviewCommentModel.Meta):
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        default_related_name = "comments"
