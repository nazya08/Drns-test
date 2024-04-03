from rest_framework import permissions


class IsAdminOrConsumer(permissions.BasePermission):
    """Клас дозволів для надання доступу до об'єкта адміністраторам або користувачам, які пов'язані з об'єктом."""
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.consumer == request.user


class IsAdminAllOrConsumerGet(permissions.BasePermission):
    """
    Клас дозволів для надання доступу до об('єкта адміністраторам для всіх методів або користувачам,
    пов'язаним з об'єктом, тільки для GET - запитів.
    """
    def has_object_permission(self, request, view, obj):
        """"""
        if request.user.is_staff:
            return True
        elif request.method == 'GET':
            return obj.goods.order.consumer == request.user
        return False
