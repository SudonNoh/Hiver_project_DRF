from rest_framework.permissions import BasePermission


class IsStaffOnly(BasePermission):
    # view 호출시 접근 권한
    # APView 접근 시 체크
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
    
    # 개별 레코드 접근 권한
    # APView 의 get_object 함수를 통해 object 획득 시 체크
    # 브라우저를 통한 API 접근시에 CREATE/UPDATE Form 노출 여부 확인 시
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.is_staff == True:
                return True
        else:
            return False