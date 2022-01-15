from django.db import models
from core.models import TimestampedModel


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
        