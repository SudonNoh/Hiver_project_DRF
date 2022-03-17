from datetime import datetime
from rest_framework import serializers

from brand.API.serializers import (
    BrandSerializer
    )

from product.models import (
    SubCategory, Category, Size, Product, Product_Image, Product_Color
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
    
    
# Color를 저장할 때 image를 같이 저장하도록 한다.
# Product를 저장한 후 옵션인 Color와 Image를 저장
# Main image는 Sales Goods에서 지정
class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(read_only=True)
    # read_only 옵션이 필요한지 여부 확인
    subcategory = SubCategorySerializer(read_only=True)
    product_number = serializers.CharField(max_length=128, read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'
        
    def create(self, validated_data):
        
        brand = self.context.get('brand', None)
        subcategory_pk = self.context.get('subcategory', None)
        subcategory = SubCategory.objects.get(pk=subcategory_pk)
        
        product = Product.objects.create(
            brand = brand,
            subcategory = subcategory
            **validated_data
        )
        
        date = datetime.today().strftime('%Y%m%d')[2:].zfill(6)
        brand_pk = str(product.brand.pk).zfill(3)
        product_pk = str(product.pk).zfill(4)
        
        product.product_number = date + brand_pk + product_pk
        product.save()
        
        return product
    
    
# Product Image Serializer
class Product_ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Image
        fields = '__all__'


# Product color Serializer
class Product_ColorSerializer(serializers.ModelSerializer):
    image = Product_ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product_Color
        fields = [
            'id',
            'product',
            'color',
            'image'
        ]
    
    def create(self, validated_data):
        
        image_data = self.context['request'].FILES
        product = self.context.get('product', None)
        
        product_color = Product_Color.objects.create(
            product = product,
            **validated_data
        )
        
        for image in image_data.getlist('image'):
            Product_Image.object.create(
                product_color = product_color, image=image
            )