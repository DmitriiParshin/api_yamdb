from django.urls import path

from users.views import signup, get_token

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('token/', get_token, name='get_token'),
]
