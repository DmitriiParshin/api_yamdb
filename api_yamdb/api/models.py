from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Title(models.Model):
    name = models.CharField(max_length=120)
    year = models.PositiveIntegerField(validators=[
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
        return self.name[:30]


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.slug


class Genre(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.slug
