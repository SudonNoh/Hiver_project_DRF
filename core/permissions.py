from rest_framework.permissions import BasePermission

# 인증 받고 groups가 'system_admin'인 경우
# permission_classes = (IsAuthenticated&IsSystemAdmin,)
# 인증 받고 groups가 'system_admin'이거나 'site_admin'인 경우에
# permission_classes = (IsAuthenticated&(IsSystemAdmin|IsSiteAdmin),)

class CustomPerm(BasePermission):
    # 명제(proposition)
    def propo(self, request, view, group_name):
        # is_superuser 인 경우 True
        if request.user.is_superuser:
            return True
        
        # is_staff 인 경우 True
        if request.user.is_staff:
            return True
        
        # group이 지정되지 않은 경우 False
        if not request.user.groups.values():
            return False
        
        # group_name이 'system_admin' 이면서 is_superuser가 아닌 경우 False
        if group_name == 'system_admin':
            if not request.user.is_superuser:
                return False
        
        # group_name이 'site_admin' 이면서 is_staff가 아닌 경우 False
        elif group_name == 'site_admin':
            if not request.user.is_staff:
                return False
                
        return bool(request.user.groups.values()[0]['name'] == group_name)

# groups가 system_admin인 경우에만 실행
class IsSystemAdmin(CustomPerm):
    # view 호출시 접근 권한
    # APView 접근 시 체크
    def has_permission(self, request, view):
        return CustomPerm.propo(self, request, view, 'system_admin')
    
    # 개별 레코드 접근 권한
    # APView 의 get_object 함수를 통해 object 획득 시 체크
    # 브라우저를 통한 API 접근시에 CREATE/UPDATE Form 노출 여부 확인 시
    def has_object_permission(self, request, view, obj):
        return CustomPerm.propo(self, request, view, 'system_admin')

# groups가 is_admin인 경우에만 실행
class IsSiteAdmin(CustomPerm):
    def has_permission(self, request, view):
        return CustomPerm.propo(self, request, view, 'site_admin')
    
    def has_object_permission(self, request, view, obj):
        return CustomPerm.propo(self, request, view, 'site_admin')

# groups가 master_vendor인 경우에만 실행
class IsMasterVendor(CustomPerm):
    def has_permission(self, request, view):
        return CustomPerm.propo(self, request, view, 'master_vendor')

    def has_object_permission(self, request, view, obj):
        return CustomPerm.propo(self, request, view, 'master_vendor')
        
# groups가 regular_vendor인 경우에만 실행
class IsGeneralVendor(CustomPerm):
    def has_permission(self, request, view):
        return CustomPerm.propo(self, request, view, 'general_vendor')

    def has_object_permission(self, request, view, obj):
        return CustomPerm.propo(self, request, view, 'general_vendor')
    
# groups가 membership_customer인 경우
class IsMemberShipCustomer(CustomPerm):
    def has_permission(self, request, view):
        return CustomPerm.propo(self, request, view, 'membership_customer')
    
    def has_object_permission(self, request, view, obj):
        return CustomPerm.propo(self, request, view, 'membership_customer')

# groups가 general_customer인 경우
class IsGeneralCustomer(CustomPerm):
    def has_permission(self, request, view):
        return CustomPerm.propo(self, request, view, 'general_vendor')
    
    def has_object_permission(self, request, view, obj):
        return CustomPerm.propo(self, request, view, 'general_vendor')