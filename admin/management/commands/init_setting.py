from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from authentication.models import User
from brand.models import Brand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print('Start init Setting')
        Brand.objects.create(brand="Admin", brand_type="Admin")
        Brand.objects.create(brand="Customer", brand_type="Customer")
        
        Group.objects.create(name="system_admin")
        Group.objects.create(name="site_admin")
        Group.objects.create(name="master_vendor")
        Group.objects.create(name="general_vendor")
        Group.objects.create(name="membership_customer")
        Group.objects.create(name="general_customer")
        
        User.objects.create_superuser(
            email = "superuser@test.com",
            username = "super",
            password = "test1234",
            phone_number = "000-0000-0000"
            )
        
        group = Group.objects.get(name="system_admin")
        user = User.objects.get(id=1)
        user.groups.add(group)
        user.brand = Brand.objects.get(id=1)
        user.save()
        print('Finished setting')