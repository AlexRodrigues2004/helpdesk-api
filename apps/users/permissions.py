from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsAttendant(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_attendant or request.user.is_admin
        )


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_client


class IsAttendantOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_attendant or request.user.is_admin
        )


class IsOwnerOrAttendant(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_attendant or request.user.is_admin:
            return True
        return obj.created_by == request.user