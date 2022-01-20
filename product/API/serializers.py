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
    brand = serializers.StringRelatedField(read_only=True)
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
class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(read_only=True)
    product_number = serializers.CharField(max_length=128, read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'brand',
            'name',
            'subcategory',
            'product_color',
            'product_number'
        ]
        depth=2
    
    # 이 부분을 수정해야 함.
    # 1. product_number가 자동으로 생성되도록 함
    # 2. subcategory가 나오면 상위 category가 나오도록 해야함
    def create(self, validated_data):
        brand = self.context.get('brand', None)
        product = Product.objects.create(
            brand=brand, 
            **validated_data
            )
        return product
        
        