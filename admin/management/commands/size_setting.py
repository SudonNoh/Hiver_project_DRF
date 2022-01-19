from django.core.management.base import BaseCommand
from brand.models import Brand
from product.models import Size


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Size.objects.create(size_name="XL", brand_id=Brand.objects.get(id=3))
        Size.objects.create(size_name="L", brand_id=Brand.objects.get(id=3))
        Size.objects.create(size_name="M", brand_id=Brand.objects.get(id=3))
        Size.objects.create(size_name="S", brand_id=Brand.objects.get(id=3))
        Size.objects.create(size_name="XL", brand_id=Brand.objects.get(id=4))
        Size.objects.create(size_name="L", brand_id=Brand.objects.get(id=4))
        Size.objects.create(size_name="M", brand_id=Brand.objects.get(id=4))
        Size.objects.create(size_name="S", brand_id=Brand.objects.get(id=4))