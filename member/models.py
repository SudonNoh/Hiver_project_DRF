from django.db import models
from core.models import TimestampedModel

# Create your models here.
class Brand(TimestampedModel):
    
    brand = models.CharField('Brand', max_length=255, unique=True)
    brand_address = models.CharField('Brand Address', max_length=255)
    brand_type = models.CharField(
        'Brand Type', 
        max_length=255, 
        choices=[
            ('Shopping_mall', 'Shopping_mall'), 
            ('Brand', 'Brand')
            ]
        )
    brand_phone_number = models.CharField('Brand Phone Number', max_length=255, unique=True)
    brand_email = models.EmailField('Brand Email')
    brand_homepage = models.URLField('Brand Homepage')
    brand_description = models.TextField('Brand Description')
    brand_logo = models.ImageField('Brand Logo')