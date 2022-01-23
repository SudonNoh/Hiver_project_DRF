from django.db import models
from core.models import TimestampedModel

# Create your models here.
class Brand(TimestampedModel):
    
    brand = models.CharField(max_length=255, unique=True)
    brand_address = models.CharField(
        max_length=255, 
        blank=True,
        )
    brand_type = models.CharField(
        max_length=255, 
        choices=[
            ('Shopping_mall', 'Shopping_mall'), 
            ('Brand', 'Brand'),
            ('Customer', 'Customer'),
            ('Admin', 'Admin')
            ]
        )
    brand_phone_number = models.CharField(max_length=255)
    brand_email = models.EmailField(blank=True)
    brand_homepage = models.URLField(blank=True)
    brand_description = models.TextField(blank=True)
    brand_logo = models.ImageField(default='media/default/Ryan.jpg', upload_to="logo/%Y/%m/%d")
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.brand