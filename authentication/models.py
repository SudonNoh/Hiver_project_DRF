import jwt
from datetime import datetime, timedelta

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from authentication.managers import UserManager
from core.models import TimestampedModel

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255, unique=True)
    # Admin : 1
    # Customer : 2
    brand = models.ForeignKey(
        'brand.Brand',
        related_name='user', 
        on_delete=models.PROTECT,
        default=2
        )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = [
        'username',
        'phone_number',
    ]
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username
    
    @property
    def token(self):
        return self._generate_jwt_token()
    
    def _generate_jwt_token(self):
        
        dt = datetime.now() + timedelta(days=30)
        
        token = jwt.encode({
            'id':self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')
        
        return token