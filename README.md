# API_YamDB

REST API для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке.

Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Произведению может быть присвоен жанр. Новые жанры может создавать только администратор.
Читатели оставляют к произведениям текстовые отзывы и выставляют произведению рейтинг (оценку в диапазоне от одного до десяти).
Из множества оценок автоматически высчитывается средняя оценка произведения.

Аутентификация по JWT-токену

Поддерживает методы GET, POST, PUT, PATCH, DELETE

Предоставляет данные в формате JSON

Cоздан в команде из трёх человек с использованим Git в рамках учебного курса Яндекс.Практикум.

## Стек технологий
- проект написан на Python с использованием Django REST Framework
- библиотека Simple JWT - работа с JWT-токеном
- библиотека django-filter - фильтрация запросов
- базы данны - SQLite3 и PostgreSQL
- автоматическое развертывание проекта - Docker, docker-compose
- система управления версиями - git

## Как запустить проект, используя Docker (база данных PostgreSQL):
1) Клонируйте репозитроий с проектом:
```
git clone https://github.com/leks20/yamdb
```
2) В директории проекта создайте файл .env, в котором пропишите следующие переменные окружения (для тестирования можете использовать указанные значения переменных):
 - SECRET_KEY='z!+4n+s%r=&z+r6v0-!_$@uger)@%$fm@)4w*x12ecw0z+%!@8'
 - DB_ENGINE=django.db.backends.postgresql
 - DB_NAME=postgres
 - DB_USER=postgres
 - DB_PASSWORD=postgres
 - DB_HOST=db
 - DB_PORT=5432
 - POSTGRES_USER=postgres
 - POSTGRES_PASSWORD=postgres
 - POSTGRES_DB=postgres
3) С помощью Dockerfile и docker-compose.yaml разверните проект:
```
docker-compose up --build
```
4) В новом окне терминала узнайте id контейнера yamdb_web и войдите в контейнер:
```
docker container ls
```
```
docker exec -it <CONTAINER_ID> bash
```
5) В контейнере выполните миграции, создайте суперпользователя и заполните базу начальными данными:
```
python manage.py migrate

python manage.py createsuperuser

python manage.py loaddata fixtures.json
```
_________________________________
Ваш проект запустился на http://0.0.0.0:8000/

Полная документация ([redoc.yaml](https://github.com/leks20/yamdb/blob/master/static/redoc.yaml)) доступна по адресу http://0.0.0.0:8000/redoc/

Вы можете запустить тесты и проверить работу модулей:
```
docker exec -ti <container_id> pytest
```

## Как запустить проект без использования Docker (база данных SQLite3):

1) Клонируйте репозитроий с проектом:
```
git clone https://github.com/leks20/yamdb
```
2) В созданной директории установите виртуальное окружение, активируйте его и установите необходимые зависимости:
```
python3 -m venv venv

. venv/bin/activate

pip install -r requirements.txt
```
3) Создайте в директории файл .env и поместите туда SECRET_KEY, необходимый для запуска проекта
   - сгенерировать ключ можно на сайте [Djecrety](https://djecrety.ir/)

4) Выполните миграции:
```
python manage.py migrate
```
5) Cоздайте суперпользователя:
```
python manage.py createsuperuser
```
6) Загрузите тестовые данные:
```
python manage.py loaddata fixtures.json
```
7) Запустите сервер:
```
python manage.py runserver
```
__________________________________

Ваш проект запустился на http://127.0.0.1:8000/

Полная документация ([redoc.yaml](https://github.com/leks20/yamdb/blob/master/static/redoc.yaml)) доступна по адресу http://127.0.0.1:8000/redoc/

С помощью команды *pytest* вы можете запустить тесты и проверить работу модулей

## Алгоритм регистрации пользователей
- Пользователь отправляет запрос с параметрами *email* и *username* на */auth/email/*.
- YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес *email* .
- Пользователь отправляет запрос с параметрами *email* и *confirmation_code* на */auth/token/*, в ответе на запрос ему приходит token (JWT-токен).

## Ресурсы API YaMDb

- Ресурс AUTH: аутентификация.
- Ресурс USERS: пользователи.
- Ресурс TITLES: произведения, к которым пишут отзывы (определённый фильм, книга или песня).
- Ресурс CATEGORIES: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
- Ресурс GENRES: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- Ресурс REVIEWS: отзывы на произведения. Отзыв привязан к определённому произведению.
- Ресурс COMMENTS: комментарии к отзывам. Комментарий привязан к определённому отзыву.
______________________________________________________________________
### Пример http-запроса (POST) для создания нового комментария к отзыву:
```
url = 'http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/'
data = {'text': 'Your comment'}
headers = {'Authorization': 'Bearer your_token'}
request = requests.post(url, data=data, headers=headers)
```
### Ответ API_YamDB:
```
Статус- код 200

{
 "id": 0,
 "text": "string",
 "author": "string",
 "pub_date": "2020-08-20T14:15:22Z"
}
```

