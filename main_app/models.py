from django.db import models
from django.contrib.auth.models import User

CLASS = (
    ('W', 'Warrior'),
    ('A', 'Archer'),
    ('R', 'Rogue')
)

class Character(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    job = models.CharField(
        max_length=1,
        choices=CLASS,
        default=CLASS[0][0]
    )
    level = models.IntegerField(default=1)
    gold = models.IntegerField(default=500)