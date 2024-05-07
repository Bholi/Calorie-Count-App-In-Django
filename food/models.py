from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    calorie = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
    protein = models.FloatField()
    def __str__(self) -> str:
        return self.name
    
class Consume(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item_name = models.ForeignKey(Item,on_delete=models.CASCADE)
    