from django.core.management.base import BaseCommand
from authentication.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user_list = User.objects.all()
        count = 0
        for i in user_list:
            count += 1
            print(
                "\n", 
                count,
                ". \n username: ", 
                i.username, 
                " :: ", 
                "\n token: ", 
                i.token,
                "\n groups: ", 
                i.groups.values()[0]['name'],
                "\n brand: ",
                i.brand.brand
                )