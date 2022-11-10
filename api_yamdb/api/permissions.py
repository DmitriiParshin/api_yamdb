from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """Для аутентифицированных пользователей имеющих статус администратора или
    персонала иначе только просмотр."""
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user.is_authenticated
                and (request.user.is_staff or request.user.is_admin))
