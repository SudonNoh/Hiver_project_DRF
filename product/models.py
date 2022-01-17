from django.db import models
from core.models import TimestampedModel
from datetime import datetime


class Category(models.Model):
    category = models.CharField(unique=True, max_length=128)
    
    
class SubCategory(models.Model):
    category = models.ForeignKey(unique=True, max_length=128)
    subcategory = models.CharField(unique=True, max_length=128)
    
    
class Product(models.Model):
    brand_id = models.ForeignKey('brand.Brand', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, unique=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    product_color = models.CharField(max_length=255)
    product_number = models.CharField(max_length=128, unique=True)
    
    # def update(self):
        
    # def save(self, *args, **kwargs):
        

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