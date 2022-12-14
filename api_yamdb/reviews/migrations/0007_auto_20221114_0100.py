# Generated by Django 2.2.16 on 2022-11-14 01:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20221112_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Оценка должна быть больше или равна 1'), django.core.validators.MaxValueValidator(10, message='Оценка должна быть меньше или равна 10')], verbose_name='Оценка произведения'),
        ),
    ]
