from django.db import models
from core.models import TimestampedModel


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey('authentication.User')
    sale_goods = models.ForeignKey('product.Sale_Goods', on_delete=models.CASCADE)
    order_quantity = models.IntegerField()
    
    def sub_total(self):
        return self.order_quantity * self.sale_goods.sale_price


# class Order(TimestampedModel):
    