from datetime import datetime
from turtle import Turtle
from rest_framework import serializers

from brand.API.serializers import (
    BrandSerializer
    )

from product.models import (
    SubCategory, Category, Size, Product, Product_image
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
    
    
# Product Image Serializer
class Product_imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_image
        fields = '__all__'


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(read_only=True)
    product_number = serializers.CharField(max_length=128, read_only=True)
    image = Product_imageSerializer(many=True, read_only=True)
    subcategory = SubCategorySerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'brand',
            'name',
            'subcategory',
            'product_color',
            'product_number',
            'image'
        ]
            
    def create(self, validated_data):
        
        images_data = self.context['request'].FILES
        brand = self.context.get('brand', None)
        subcategory_pk = self.context.get('subcategory', None)
        subcategory = SubCategory.objects.get(pk=subcategory_pk)

        product = Product.objects.create(
            brand = brand,
            subcategory = subcategory,
            **validated_data
            )
        
        for image_data in images_data.getlist('image'):
            Product_image.objects.create(product=product, image=image_data)
        
        date = datetime.today().strftime('%Y%m%d')[2:].zfill(6)
        brand_pk = str(product.brand.pk).zfill(3)
        product_pk = str(product.pk).zfill(4)

        product.product_number = date + brand_pk + product_pk
        product.save()
        
        return product
    
    
# Postman 으로 요청했을 때 image 에 대한 내용이 나오지 않음.
# Article 프로젝트를 보고 수정해야함 image가 나오도록.
# TagRelated 필드와 같이 필드를 따로 만들어야함