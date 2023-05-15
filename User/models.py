from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from . import manager


# Create your models here.

class User(AbstractUser):
    username = None
    phone = PhoneNumberField(unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.TextField()
    user_profile_image = models.ImageField(upload_to='media/user/profile')
    last_login = models.DateTimeField(null=True, blank=True)

    objects = manager.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Address(models.Model):
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=255)
    street_2 = models.CharField(max_length=255)
    land_mark = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


class UserAddress(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
