from rest_framework import serializers

from brand.models import Brand


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