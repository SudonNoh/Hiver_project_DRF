from rest_framework import serializers
from brand.API.serializers import BrandSerializer

from authentication.models import User
from brand.models import Brand


class AdminUserSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    
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
            'created_at',
            'updated_at',
        ]
        # depth = 1
        
    # def update(self, instance, validated_data):
    #     print("\n\n validated_data : ", validated_data)
    #     print("\n\n validated_data : ", validated_data['brand'])
    #     print("\n\n instance : ", instance, "\n\n")
        
    #     brand = validated_data.pop('brand')
        
    #     instance.brand = brand.id
    #     return instance


class AdminBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'id',
            'brand',
            'brand_address',
            'brand_type',
            'brand_phone_number',
            'brand_email',
            'brand_homepage',
            'brand_description',
            'brand_logo'
        ]