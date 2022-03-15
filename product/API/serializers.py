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
    
    
# Product Image Serializer
class Product_ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Image
        fields = '__all__'


# Product, Size , Image, Color, Goods, Sale_goods
# 1. Color에 대한 Serializer를 우선 생성한다.
class Product_ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Color
        fields = '__all__'
        
# 2. Product 만들 때 Color, Image 같이 만들어지도록 한다.
class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(read_only=True)
    product_number = serializers.CharField(max_length=128, read_only=True)
    product_color = Product_ColorSerializer(many=True, read_only=True)
    product_image = Product_ImageSerializer(many=True, read_only=True)
    subcategory = SubCategorySerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'brand',
            'name',
            'subcategory',
            'product_color',
            'product_image',
            'product_number'
        ]
    
    def create(self, validated_data):
        
        
    
# 3. Goods Serializer
# 4. Sale_goods Serializer



# Product Serializer
# class ProductSerializer(serializers.ModelSerializer):
#     brand = serializers.StringRelatedField(read_only=True)
#     product_number = serializers.CharField(max_length=128, read_only=True)
#     image = Product_ImageSerializer(many=True, read_only=True)
#     subcategory = SubCategorySerializer(read_only=True)
    
#     class Meta:
#         model = Product
#         fields = [
#             'id',
#             'brand',
#             'name',
#             'subcategory',
#             'product_color',
#             'product_number',
#             'image',
#         ]
            
#     def create(self, validated_data):
        
#         images_data = self.context['request'].FILES
#         brand = self.context.get('brand', None)
#         subcategory_pk = self.context.get('subcategory', None)
#         subcategory = SubCategory.objects.get(pk=subcategory_pk)

#         product = Product.objects.create(
#             brand = brand,
#             subcategory = subcategory,
#             **validated_data
#             )
        
#         # 첫번째 들어오는 image_data를 main으로 저장
#         cnt = 0
#         for image_data in images_data.getlist('image'):
#             cnt += 1
#             if cnt == 1:
#                 Product_Image.objects.create(
#                     product=product, image=image_data, is_main=True
#                     )
#             else:
#                 Product_Image.objects.create(product=product, image=image_data)
                
#         date = datetime.today().strftime('%Y%m%d')[2:].zfill(6)
#         brand_pk = str(product.brand.pk).zfill(3)
#         product_pk = str(product.pk).zfill(4)

#         product.product_number = date + brand_pk + product_pk
#         product.save()
        
#         return product
