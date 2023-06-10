from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Name=models.CharField(max_length=200,null=True,unique=True)
    Location=models.CharField(max_length=200,null=True)
    Preference=models.CharField(max_length=200,null=True)

    USERNAME_FIELD='Name'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.username
    