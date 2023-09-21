from django.db import models

# Create your models here.
class Enric(models.Model):
    name=models.CharField(max_length=100)
    review=models.CharField()