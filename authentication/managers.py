from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self, username, email, is_member, brand, password=None, **extra_fields):
        
        if username is None:
            raise TypeError('Users must have a username')
        
        if email is None:
            raise TypeError('Users must have an email address')

        if password is None:
            raise TypeError('Users must have a password')
        
        if is_member == True:
            raise TypeError('Members must set a brand')
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            **extra_fields
        )
        
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):
        
        if password is None:
            raise TypeError('Superuser must have a password')
        
        user = self.create_user(username, email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user