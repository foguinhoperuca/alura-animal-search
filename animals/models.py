from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=50)
    predator = models.CharField(max_length=5)
    poisonous = models.CharField(max_length=5)
    domestic = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name}"
