from rest_framework import permissions


class OwnerPermission(permissions.BasePermission):
    """
    해당 자원의 소유자 (user)만 API를 수정할 수 있도록 권한 정의
    """

    def has_permission(self, request, view):
        # Any requests are allowed only if the user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the resource
        return request.user.is_superuser or obj.user == request.user
