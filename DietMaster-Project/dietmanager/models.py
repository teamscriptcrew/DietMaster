from django.db import models

# Create your models here.
class HealthModel(models.Model):
    username = models.CharField(max_length=30, unique=True)
    age = models.IntegerField()
    isMale = models.BooleanField()
    isFemale = models.BooleanField()
    weight = models.CharField(max_length=30)
    height = models.CharField(max_length=30)
    isActive = models.BooleanField()
    isnotActive = models.BooleanField()
    isModeratelyActive = models.BooleanField()