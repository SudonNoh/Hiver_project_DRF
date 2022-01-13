from django.db import models
from core.models import TimestampedModel

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)
    
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=255)
    
    
# Vendor가 올리는 것들은 Brand가 들어가도록 한다.
class Product(TimestampedModel):
    brand = models.ForeignKey('brand.Brand', on_delete=models.CASCADE)
    product_number = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    