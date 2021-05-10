from django.db import models

# Create your models here.

class Date(models.Model):
    enterDate = models.TextField()
    exitDate = models.TextField()
    rank = models.TextField()
    