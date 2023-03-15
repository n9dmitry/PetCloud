from django.db import models
from registr.models import Profile


class Post(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True,)
    time = models.TimeField(auto_now=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title