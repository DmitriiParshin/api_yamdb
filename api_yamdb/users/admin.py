from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'first_name',
              'last_name', 'bio', 'role')

    list_display = ('username', 'email', 'first_name',
                    'last_name', 'bio', 'role')


admin.site.register(User, UserAdmin)
