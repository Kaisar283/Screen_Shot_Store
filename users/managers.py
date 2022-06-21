from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class NewUserManagger(BaseUserManager):
    def create_user(self, email, user_name, password=None, **extra_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **extra_fields)
        if password is None:
            raise ValueError('ERROR: The username must have a password')
        else:
            user.set_password(password)
        user.save()
        return user

    def _create_user(self, email, user_name, password=None, **extra_field):
        user = self.model(email=email, user_name=user_name, **extra_field)
        user.is_active = True
        user.set_password(password)
        return user.save()

    def create_superuser(self, email, user_name, password=None, **extra_field):
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_active', True)

        if extra_field.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if extra_field.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        return self._create_user(email, user_name, **extra_field)
