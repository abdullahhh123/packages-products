from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']



class Package(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()

    def __str__(self):
        return self.product_price

class Subscription(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    package_ids = models.ManyToManyField(Package)
