from django.contrib.auth import get_user, get_user_model
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        print('print')
        if request.user.is_authenticated:
            if request.user.is_staff == True:
                return True
        else:
            return False