from rest_framework import serializers

from brand.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    # brand_logo = serializers.ImageField(use_url=True)
    class Meta:
        model = Brand
        fields = [
            'brand',
            'brand_address',
            'brand_type',
            'brand_phone_number',
            'brand_email',
            'brand_homepage',
            'brand_description',
            'brand_logo'
        ]
        
        read_only_fields = [
            'brand',
            'brand_type',
            'brand_phone_number'
        ]
        
    def update(self, instance, validated_data):
        
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        
        instance.save()
        
        return instance