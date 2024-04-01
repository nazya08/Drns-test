from rest_framework import permissions


class IsAdminOrCraftsman(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.craftsman == request.user
