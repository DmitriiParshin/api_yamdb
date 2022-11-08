from django.contrib import admin

from reviews.models import Review, Comment


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'author', 'score', 'pub_date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'review', 'text', 'author', 'pub_date')


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
