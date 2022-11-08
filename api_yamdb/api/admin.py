from django.contrib import admin

from api.models import Title, Category, Genre
from users.models import User


class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'bio', 'role')
    empty_value_display = "-пусто-"


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'year')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'bio', 'role')
    empty_value_display = "-пусто-"


admin.site.register(Title, TitleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(User, UserAdmin)
