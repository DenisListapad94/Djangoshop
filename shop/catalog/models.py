from django.db import models

class Clothes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    size = models.IntegerField()
    color = models.CharField(max_length=100)
    def __str__(self):
        return self.name
