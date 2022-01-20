from wsgiref import validate
from rest_framework import serializers

from brand.API.serializers import (
    BrandSerializer
)
from product.models import (
    Size, 
    Product
    )

# Size Serializer
class SizeSerializer(serializers.ModelSerializer):
    # brand_id = BrandSerializer(read_only=True)
    brand = serializers.StringRelatedField()
    class Meta:
        model = Size
        fields = [
            'id',
            'size_name',
            'brand'
            ]
    
    def create(self, validated_data):
        brand = self.context.get('brand', None)
        size = Size.objects.create(brand=brand, **validated_data)
        return size
    
# Product Serializer