from rest_framework import permissions


class CustomUserPermission(permissions.BasePermission):
    """
    사용자 API 접근 권한 정의
    """
    message = '해당 사용자에 대한 접근 권한이 없습니다.'

    def has_object_permission(self, request, view, obj):
        # 관리자 권한이 있으면 접근 가능
        is_superuser = request.user.is_superuser
        if is_superuser:
            return True

        # 로그인하지 않았을 경우에만 회원 가입 (사용자 생성) 가능
        if not (request.user.is_authenticated) and request.method in ['POST']:
            return True

        # 수정/삭제 (PUT/PATCH/DELETE)는 해당 사용자로 로그인한 경우에만 접근 가능
        is_logged_in_as_user = obj.id == request.user.id
        if request.method in request.method in ['PUT', 'PATCH', 'DELETE']:
            return is_logged_in_as_user

        # 그 외의 경우에는 로그인한 경우에만 접근 가능
        return request.user.is_authenticated
