from django.contrib import admin
from django.contrib.admin.views.main import ChangeList

from reviews.forms import GenreChangeListForm
from reviews.models import Title, Category, Genre, Review, Comment


class GenreChangeList(ChangeList):
    def __init__(self, request, model, list_display, list_display_links,
                 list_filter, date_hierarchy, search_fields,
                 list_select_related, list_per_page, list_max_show_all,
                 list_editable, model_admin, sortable_by):
        super(GenreChangeList, self).__init__(request, model, list_display,
                                              list_display_links, list_filter,
                                              date_hierarchy, search_fields,
                                              list_select_related,
                                              list_per_page, list_max_show_all,
                                              list_editable, model_admin,
                                              sortable_by)
        self.list_display = ('id', 'name', 'year', 'description', 'category',
                             'genre')
        self.list_display_links = ('name', 'category')
        self.list_editable = ('genre',)
        self.search_fields = ('name', 'year')
        self.list_select_related = ('category', 'genre')


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    def get_changelist(self, request, **kwargs):
        return GenreChangeList

    def get_changelist_form(self, request, **kwargs):
        return GenreChangeListForm


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
