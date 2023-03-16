from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    """Модель профиля"""
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email = models.EmailField(max_length = 254)

    def __str__(self):
        return self.user.username

