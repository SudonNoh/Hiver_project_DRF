from rest_framework.permissions import BasePermission


class IsStaffOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.is_staff == True:
                return True
        else:
            return False