from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    credit_card = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.username
