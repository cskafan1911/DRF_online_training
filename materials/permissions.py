from rest_framework import permissions


class IsUserIsOwner(permissions.BasePermission):
    """
    Класс прав доступа для владельца контента.
    """

    message = 'Вы не являетесь владельцем контента'

    def has_object_permission(self, request, view, obj):
        """
        Метод для проверки, является ли пользователь владельцем контента.
        """
        return obj.user == request.user


class IsModerator(permissions.BasePermission):
    """
    Класс прав доступа для модератора.
    """

    def has_permission(self, request, view):
        """
        Метод для проверки, входит ли пользователь в группе модераторов.
        """
        if request.user.groups.filter(name='moderator').exists():
            return True
        return False
