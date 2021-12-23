from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self, username, email, password=None, **extra_fields):
        
        if username is None:
            raise TypeError('Users must have a username')
        
        if email is None:
            raise TypeError('Users must have an email address')

        if password is None:
            raise TypeError('Users must have a password')
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            **extra_fields
        )
        
        user.set_password(password)
        user.save()
        return user