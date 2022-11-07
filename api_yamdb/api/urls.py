from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CategoryViewSet, GenreViewSet, TitleViewSet,
                       signup, get_token)

router_v1 = DefaultRouter()
router_v1.register(r'categories', CategoryViewSet)
router_v1.register(r'genres', GenreViewSet)
router_v1.register(r'titles', TitleViewSet)


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', signup, name='signup'),
    path('v1/auth/token/', get_token, name='get_token'),
]
