from datetime import datetime
from turtle import Turtle
from rest_framework import serializers
from product.models import SubCategory, Category

from brand.API.serializers import (
    BrandSerializer
    )

from product.models import (
    Size, Product
    )


# SubCategory/CategorySerializer
# ProductSerializer에서 get할 때 Subcategory 및 Category내용을
# 불러오기 위함
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
        depth=1
    
    
# Size Serializer
class SizeSerializer(serializers.ModelSerializer):
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
    subcategory = SubCategorySerializer(read_only=True)
    
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
            
    def create(self, validated_data):

        brand = self.context.get('brand', None)
        subcategory_pk = self.context.get('subcategory', None)
        subcategory = SubCategory.objects.get(pk=subcategory_pk)

        product = Product.objects.create(
            brand = brand,
            subcategory = subcategory,
            **validated_data
            )
        
        date = datetime.today().strftime('%Y%m%d')[2:].zfill(6)
        brand_pk = str(product.brand.pk).zfill(3)
        product_pk = str(product.pk).zfill(4)

        product.product_number = date + brand_pk + product_pk
        product.save()
        
        return product