from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField("Электронная почта",unique=True)
    phone_number = models.CharField("Номер телефона",max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

