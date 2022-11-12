from django.contrib import admin

from reviews.models import Title, Category, Genre, Review, Comment


class GenreInline(admin.TabularInline):
    model = Title.genre.through


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    inlines = (GenreInline, )
    list_display = ('id', 'name', 'year', 'description', 'category',
                    'get_genre')
    list_display_links = ('name',)
    list_editable = ('category',)
    search_fields = ('name', 'year')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'author', 'score', 'pub_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'review', 'text', 'author', 'pub_date')
