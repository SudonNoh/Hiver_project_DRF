from django.db import models
from core.models import TimestampedModel
from datetime import datetime

# Category, SubCategory 모델 생성 및 수정, 삭제는 system_admin , site_admin 수준에서 진행
class Category(models.Model):
    category = models.CharField(unique=True, max_length=128)
    
    
class SubCategory(models.Model):
    category = models.ForeignKey(unique=True, max_length=128)
    subcategory = models.CharField(unique=True, max_length=128)
    
    
# 이하 단계에서는 각 브랜드 수준에서 진행
class Product(models.Model):
    brand_id = models.ForeignKey('brand.Brand', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    product_color = models.CharField(max_length=255)
    # Serializers.py 에서 자동으로 입력되도록 구현
    product_number = models.CharField(max_length=128, blank=True)

'''
예시
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    original_number = models.CharField(max_length=255, blank=True)
    
    def update_model(self):
        print(self.title)
        print(self.id) 
        print(type(self.id))
        Post.objects.filter(id=self.id).update(original_number=str(self.id)+datetime.today().strftime('%Y%m%d'))

    def save(self, *args, **kwargs):
        self.original_number = self.title
        super(Post, self).save(*args, **kwargs)
        self.update_model()
'''

class Size(models.Model):
    size_name = models.CharField(max_length=128, unique=True)
    brand_id = models.ForeignKey('brand.Brand', on_delete=models.CASCADE)
    

class Measurement(models.Model):
    measurement = models.CharField(max_length=128, unique=True)


class Part(models.Model):
    part = models.CharField(max_length=128)
    measurement = models.ManyToManyField('product.Measurement', related_name='part')


class Goods(models.Model):
    size_id = models.ForeignKey('product.Size', on_delete=models.PROTECT)
    product_id = models.ForeignKey('product.Product')