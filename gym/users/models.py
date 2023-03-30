from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    )
# from django.contrib.auth import get_user_model
# User = get_user_model()

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **kwargs):
        user = self.model(username=username, email=email, **kwargs)
        user.set_password(password)
        user.save(using=self)

        return user



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique= True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

