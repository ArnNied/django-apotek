from django.db import models
from django.utils import timezone

# Create your models here.

class Role(models.Model):
    role = models.IntegerField(default=0)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

class User(models.Model):
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    register_date = models.DateTimeField()
    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    def __str__(self):
        return self.email


