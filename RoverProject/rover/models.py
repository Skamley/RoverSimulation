from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Environment Model
class Environment(models.Model):
    temperature = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    SOLAR_CHOICES = [
        (True, 'true'),
        (False, 'false'),
    ]
    solar_flare = models.BooleanField(choices=SOLAR_CHOICES)
    STORM_CHOICES = [
        (True, 'true'),
        (False, 'false'),
    ]
    storm = models.BooleanField(choices=STORM_CHOICES)
    terrain = models.CharField(max_length=100)

    def __str__(self):
        return self.terrain

#Rover model, holds all the input parameters to equip the rover
class RoverDesc(models.Model):
    name = models.CharField(max_length=100)
    location_horizontal= models.IntegerField(default=1)
    location_vertical = models.IntegerField(default=3)
    battery = models.IntegerField(default=11)
    InventoryType_CHOICES = [
        ('storm_shield', 'storm_shield'),
        ('water_sample', 'water_sample'),
        ('rock_sample', 'rock_sample'),
    ]
    InventoryQuantity_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
    ]
    inventory_type = models.CharField(choices=InventoryType_CHOICES,max_length=100)
    inventory_quantity= models.IntegerField(choices=InventoryQuantity_CHOICES)
    STORM =1
    WATER=2
    ROCK=3
    PRIORITIES = (
        (ROCK, 'Low'),
        (WATER, 'Normal'),
        (STORM, 'High'),
    )
    inventory_priority = models.IntegerField(choices=PRIORITIES)

    def __str__(self):
        return self.name

#Rover movement model to hold the status of recent movement of the rover(if applicable)
class RoverMovement(models.Model):
    #myRover = models.ForeignKey(RoverDesc, on_delete=models.CASCADE)
    direction_options = [
        ('up', 'up'),
        ('down', 'down'),
        ('left', 'left'),
        ('right', 'right'),
    ]
    direction = models.CharField(choices=direction_options,max_length=100)
    def __str__(self):
        return self.direction