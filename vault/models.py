from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pass(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    password = models.CharField(max_length=30)
    username = models.CharField(max_length=25)

    def __str__(self):
        return self.name