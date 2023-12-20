from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Character(models.Model):
    name = models.CharField(max_length=100)
    char_class = models.CharField(max_length=100)

    def __str__(self):
        return self.name