from django.contrib import admin

from reviews.models import Title, Category, Genre, Review, Comment


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    filter_horizontal = ('genre',)
    fields = ('id', 'name', 'year', 'description', 'category', 'genre')
    list_display = ('id', 'name', 'year', 'description', 'category')
    list_display_links = ('name', 'category')
    search_fields = ('name', 'year')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'author', 'score', 'pub_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'review', 'text', 'author', 'pub_date')
