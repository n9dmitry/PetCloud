from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Profile(AbstractUser):
    """Модель профиля"""
    email = models.EmailField(max_length = 254, unique= True)
    avatar = models.ImageField(upload_to= 'media/avatar/', blank= True, null = True)

    def __str__(self):
        return self.username


