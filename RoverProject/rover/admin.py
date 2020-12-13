from django.contrib import admin
from rover.models import Environment,RoverDesc,RoverMovement

# Register your models here.
admin.site.register(Environment)
admin.site.register(RoverDesc)
admin.site.register(RoverMovement)