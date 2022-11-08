import csv

from django.core.management import BaseCommand

from api.models import Category, Genre, Title
from reviews.models import Review, Comment
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('static/data/category.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            Category.objects.all().delete()
            for row in reader:
                category = Category.objects.create(id=row[0], name=row[1],
                                                   slug=row[2])
                category.save()

        with open('static/data/genre.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            Genre.objects.all().delete()
            for row in reader:
                genre = Genre.objects.create(id=row[0], name=row[1],
                                             slug=row[2])
                genre.save()

        with open('static/data/titles.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            Title.objects.all().delete()
            for row in reader:
                title = Title.objects.create(id=row[0], name=row[1],
                                             year=row[2], category_id=row[3])
                title.save()

        with open('static/data/genre_title.csv', 'r',
                  encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                title = Title.objects.get(id=row[1])
                genre = Genre.objects.get(id=row[2])
                title.genre.add(genre)
                title.save()


        with open('static/data/users.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            User.objects.all().delete()
            for row in reader:
                user = User.objects.create(id=row[0], username=row[1],
                                           email=row[2], role=row[3],
                                           bio=row[4], first_name=row[5],
                                           last_name=row[6])
                user.save()

        with open('static/data/review.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            Review.objects.all().delete()
            for row in reader:
                review = Review.objects.create(id=row[0], title_id=row[1],
                                               text=row[2],
                                               author_id=row[3],
                                               score=row[4],
                                               pub_date=row[5])
                review.save()

        with open('static/data/comments.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            Comment.objects.all().delete()
            for row in reader:
                comment = Comment.objects.create(id=row[0], review_id=row[1],
                                                 text=row[2],
                                                 author_id=row[3],
                                                 pub_date=row[4])
                comment.save()
