from rest_framework import serializers

from product.models import (
    Size, 
    Product
    )

# Size Serializer
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        models = Size
        fields = [
            'id',
            'size_name'
            ]
    
# Product Serializer