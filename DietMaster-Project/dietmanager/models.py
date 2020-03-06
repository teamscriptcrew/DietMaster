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
    diseases = models.CharField(max_length=30,default="None")
    calories = models.FloatField(default=0)
    proteins = models.FloatField(default=0)
    fats = models.FloatField(default=0)
    carbs = models.FloatField(default=0)

class StorageModel(models.Model):
    username = models.ForeignKey('HealthModel',on_delete=models.CASCADE)
    calories_to_take = models.IntegerField(default=0,unique=False)