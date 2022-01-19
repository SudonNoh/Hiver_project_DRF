from rest_framework import serializers

from authentication.models import User
from brand.models import Brand
from django.contrib.auth.models import Group
from product.models import Category, SubCategory


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
    # group, last_login, created_at, updated_at 등의 
    # 값을 확인하기 위해 Fields를 따로 정의
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


# 위의 Serializer에서 검색할 때 groups, brand의 depth=1 수준의
# 값들을 불러오지 못해서 따로 NestedAdminUserSerializer를 정의함
# depth=1을 위 Serializer에서 정의하면 Post, Patch 등 데이터 수정
# Request를 보낼 때 어려움이 있음.
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
        
        
class AdminCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

class AdminSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'