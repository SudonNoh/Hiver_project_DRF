from rest_framework import serializers

from brand.models import Brand


class BrandSerializer(serializers.ModelSerializer):
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
        ]
        
        read_only_fields = [
            'brand',
            'brand_type',
            'brand_phone_number'
        ]
        
    # def update(self, instance, validated_data):
    #     print(instance)
    #     print(validated_data.items())
        
    #     for (key, value) in validated_data.items():
    #         setattr(instance, key, value)
        
    #     instance.save()
    #     return instance