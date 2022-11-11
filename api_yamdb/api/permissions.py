from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """Для аутентифицированных пользователей имеющих статус администратора или
    персонала иначе только просмотр."""
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user.is_authenticated
                and request.user.is_admin)


class IsAdminOrOwnerOrReadOnly(BasePermission):
    """Для аутентифицированных пользователей имеющих статус администратора или
    автора запроса иначе только просмотр."""
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or request.user.is_admin
                or request.user.is_moderator
                or obj.author == request.user)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.is_admin
                or request.user.is_superuser)
