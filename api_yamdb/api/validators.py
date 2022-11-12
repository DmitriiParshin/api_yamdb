from django.core import exceptions
from django.core.validators import RegexValidator
from datetime import datetime
from django.core import exceptions


def get_year_now():
    return datetime.now().year


def username_me(value):
    if value == 'me':
        raise exceptions.ValidationError(
            'Имя пользователя "me" использовать нельзя!'
        )
    return value


class UsernameValidator(RegexValidator):
    regex = r'^[\w.@+-]+\Z'
    message = ('Недопустимые символы в имени пользователя. '
               'Используйте не более 150 символов. '
               'Только буквы, цифры и @/./+/-/_')
    code = 'invalid_format'
