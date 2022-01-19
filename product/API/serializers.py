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
    brand_id = BrandSerializer(read_only=True)
    class Meta:
        model = Size
        fields = [
            'id',
            'size_name',
            'brand_id'
            ]
        # depth=1
    
    def create(self, validated_data):
        brand_id = self.context.get('brand_id', None)
        size = Size.objects.create(brand_id=brand_id, **validated_data)
        return size
    
# Product Serializer