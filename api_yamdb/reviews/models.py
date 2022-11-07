from django.contrib.auth import get_user_model
from django.db import models

from api.models import Title

User = get_user_model()
OUTPUT_LENGTH = 100


class Review(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )
    score = models.IntegerChoices(choices=list(range(1, 11)), unique=True)

    def __str__(self):
        return self.text[:OUTPUT_LENGTH]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    title = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    def __str__(self):
        return self.text[:OUTPUT_LENGTH]

"""
class Score(models.Model):
    value = models.SmallIntegerField('Значение', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Оценка'
        ordering = ['-value']


class Rating(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ratings'
    )
    score = models.ForeignKey(
        Score, on_delete=models.CASCADE, related_name='ratings'
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='ratings'
    )
"""