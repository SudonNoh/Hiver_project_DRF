from rest_framework import serializers

from authentication.models import User
from brand.models import Brand
from django.contrib.auth.models import Group


class AdminGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
        
        
class AdminBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
        
        
class AdminUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 128,
        min_length = 8,
        write_only = True
    )
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'phone_number',
            'groups',
            'brand',
            'last_login',
            'is_active',
            'is_staff',
            'created_at',
            'updated_at',
        ]


class NestedAdminUserSerializer(serializers.ModelSerializer):
    brand = AdminBrandSerializer()
    groups = AdminGroupSerializer(many=True)
    
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'phone_number',
            'groups',
            'brand',
            'last_login',
            'is_active',
            'is_staff',
            'is_superuser',
            'created_at',
            'updated_at',
        ]