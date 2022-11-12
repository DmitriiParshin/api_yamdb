from datetime import datetime

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core import exceptions


def get_year_now():
    return datetime.now().year


class UsernameRegexValidator(UnicodeUsernameValidator):
    regex = r'^[\w.@+-]+\Z'
    flags = 0


def username_me(value):
    if value == 'me':
        raise exceptions.ValidationError(
            'Имя пользователя "me" использовать нельзя!'
        )
    return value
