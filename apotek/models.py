from django.db import models
from django.utils import timezone
from django.contrib import auth

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='apotek/img/product')
    dosage = models.CharField(max_length=255, default="Not Strict")
    quantity = models.IntegerField(default=0)
    tags = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name