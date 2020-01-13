from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, User
import datetime

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='apotek/img/product')
    description = models.TextField(blank=True)
    dosage = models.CharField(max_length=255, default="Not Strict")
    quantity = models.PositiveIntegerField(default=0)
    tags = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(default=0)
    date_added = models.DateField(auto_now=True)
    date_modified = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class ApotekUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='apotek/img/user', blank=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=(('FEMALE', 'Female'), ('MALE', 'Male')), max_length=255)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username