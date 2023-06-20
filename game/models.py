# game/models.py
from django.db import models

class Level(models.Model):
    name = models.CharField(max_length=100)
    # Other fields and relationships as needed

class Player(models.Model):
    name = models.CharField(max_length=100)
    current_level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    # Other fields and relationships as needed
