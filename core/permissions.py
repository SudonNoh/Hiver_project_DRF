from rest_framework.permissions import BasePermission

# 인증 받고 groups가 'system_admin'인 경우
# permission_classes = (IsAuthenticated&IsSystemAdmin,)
# 인증 받고 groups가 'system_admin'이거나 'site_admin'인 경우에
# permission_classes = (IsAuthenticated&(IsSystemAdmin|IsSiteAdmin),)

# groups가 system_admin인 경우에만 실행
class IsSystemAdmin(BasePermission):
    # view 호출시 접근 권한
    # APView 접근 시 체크
    def has_permission(self, request, view):
        return bool(
            request.user.is_superuser and 
            request.user.groups.name == 'system_admin'
            )
    
    # 개별 레코드 접근 권한
    # APView 의 get_object 함수를 통해 object 획득 시 체크
    # 브라우저를 통한 API 접근시에 CREATE/UPDATE Form 노출 여부 확인 시
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_superuser and 
            request.user.groups.name == 'system_admin'
            )

# groups가 is_admin인 경우에만 실행
class IsSiteAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_admin and 
            request.user.groups.name == 'site_admin'
            )
        
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_admin and 
            request.user.groups.name == 'site_admin'
            )
        
# groups가 master_vendor인 경우에만 실행
class IsMasterVendor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.groups.name == 'master_vendor')


    def has_object_permission(self, request, view, obj):
        return bool(request.user.groups.name == 'master_vendor')
        
# groups가 regular_vendor인 경우에만 실행
class IsGeneralVendor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.groups.name == 'general_vendor')
    
    def has_object_permission(self, request, view, obj):
        return bool(request.user.groups.name == 'general_vendor')
    
# groups가 membership_customer인 경우
class IsMemberShipCustomer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.groups.name == 'membership_customer')
    
    def has_object_permission(self, request, view, obj):
        return bool(request.user.groups.name == 'membership_customer')
    
# groups가 general_customer인 경우
class IsGeneralCustomer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.groups.name == 'general_customer')
    
    def has_object_permission(self, request, view, obj):
        return bool(request.user.groups.name == 'general_customer')
    