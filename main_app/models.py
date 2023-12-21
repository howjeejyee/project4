from django.db import models
from django.contrib.auth.models import User

CLASS = (
    ('W', 'Warrior'),
    ('A', 'Archer'),
    ('R', 'Rogue')
)

class Class(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    weapon = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Character(models.Model):
    name = models.CharField(max_length=100)
    char_class = models.CharField(
        max_length=1,
        choices=CLASS,
        default=CLASS[0][0]
    )

    classjob = models.ForeignKey(
        Class,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name