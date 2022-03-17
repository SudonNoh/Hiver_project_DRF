from dataclasses import field
from django.db import models
from core.models import TimestampedModel

# Category, SubCategory 모델 생성 및 수정, 삭제는 system_admin , site_admin 수준에서 진행
class Category(models.Model):
    category = models.CharField(unique=True, max_length=128)
    
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.CharField(max_length=128)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["category", "subcategory"],
                name = "Unique_Category"
            )
        ]
    
    def __str__(self):
        return self.subcategory
    
    
# 이하 단계에서는 각 브랜드 수준에서 진행
class Product(models.Model):
    brand = models.ForeignKey('brand.Brand', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    # Serializers.py 에서 자동으로 입력되도록 구현
    product_number = models.CharField(max_length=128, blank=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["brand", "name"],
                name = "Unique_Product"
            )
        ]


class Product_Color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_color')
    color = models.CharField(max_length=128)


class Product_Image(models.Model):
    product_color = models.ForeignKey(Product_Color, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(default='media/default/Ryan.jpg', upload_to="product/image/%Y/%m/%d")


class Size(models.Model):
    # XL, L, M, S, 110, 105, 100, 95 etc.
    size_name = models.CharField(max_length=128)
    brand = models.ForeignKey('brand.Brand', on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["size_name", "brand"],
                name = "Unique_Size"
            )
        ]
    
    
class Goods(models.Model):
    size = models.ForeignKey('product.Size', on_delete=models.PROTECT)
    product_color = models.ForeignKey('product.Product_Color', on_delete=models.PROTECT)
    price = models.IntegerField()
    quantity = models.IntegerField()
    

class Sale_Goods(TimestampedModel):
    title = models.CharField(max_length=255)
    content_text = models.TextField(max_length=255)
    content_image1 = models.ImageField()
    content_image2 = models.ImageField()
    goods = models.ManyToManyField(Goods)
    sale_price = models.IntegerField()
    is_active = models.BooleanField(default=True)
