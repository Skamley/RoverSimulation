from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rover.models import  Environment,RoverDesc,RoverMovement
from .import forms
from rover.forms import  EnvironmentConfigForm,RoverDescForm,RoverMovementForm
from django.views.generic import  ListView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.
def EnvironmentConfiguration(request):
    #envs = Environment.objects.all()
    Env = Environment.objects.get(pk=1)
    Context_Dir= {
            "temperature": Env.temperature,
             "humidity": Env.humidity,
             "solar_flare": Env.solar_flare,
             "storm": Env.storm,
             "terrain": Env.terrain,
    }
    return render(request, 'rover/EnvironmentConfig.html', Context_Dir)
    #return render(request, 'rover/EnvironmentConfig.html', {'index': envs,})

def EnvironmentUpdate(request):
    #form = EnvironmentConfigForm
    if request.method == 'POST':
        print("Request type is post")
        getReferenceObject = get_object_or_404(Environment, pk=1)
        form = EnvironmentConfigForm(request.POST,instance=getReferenceObject)
        #form = EnvironmentConfigForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            # return Environment(request)
            return render(request, 'rover/EnvironmentUpdate.html', {'form': form})
        else:
            print("Form is Invalid")
            return render(request, 'rover/EnvironmentUpdate.html', {'form': form})
    else:
        #model= Environment()
        make = get_object_or_404(Environment, pk=1)
        form = EnvironmentConfigForm(instance=make)
        return render(request, 'rover/EnvironmentUpdate.html', {'form': form})

def RoverConfiguration(request):
    if request.method == 'POST':
        print("Request type is post")
        getReferenceObject = get_object_or_404(RoverDesc, pk=1)
        form = RoverDescForm(request.POST,instance=getReferenceObject)
        #form = EnvironmentConfigForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            # return Environment(request)
            return render(request, 'rover/RoverConfig.html', {'form': form})
        else:
            print("Form is Invalid")
            return render(request, 'rover/RoverConfig.html', {'form': form})
    else:
        #model= Environment()
        getReferenceObject = get_object_or_404(RoverDesc, pk=1)
        form = RoverDescForm(instance=getReferenceObject)
        return render(request, 'rover/RoverConfig.html', {'form': form})

def RoverStatus(request):
    Env = Environment.objects.get(pk=1)
    RoverObj = RoverDesc.objects.get(pk=1)
    if Env.storm == True:
        #stormCheck="Cannot move during a storm"
        stormCheck=True
    else:
        stormCheck=False
    Context_Dir = {"Line1": "This site is undergoing development. Thanks for being patient.",
                }

    Context_Dir = {
        "location_horizontal": RoverObj.location_horizontal,
        "location_vertical": RoverObj.location_vertical,
        "battery": RoverObj.battery,
        "inventory_quantity": RoverObj.inventory_quantity,
        "temperature": Env.temperature,
        "humidity": Env.humidity,
        "solar_flare": Env.solar_flare,
        "storm": stormCheck,
        "terrain": Env.terrain,
    }
    return render(request, 'rover/RoverStatus.html',Context_Dir)

def RoverMove(request):
    RoverObj = RoverDesc.objects.get(pk=1)
    direction = RoverMovement.objects.get(pk=1)
    if request.method == 'POST':
        print("Request type is post")
        getReferenceObject = get_object_or_404(RoverMovement, pk=1)
        form = RoverMovementForm(request.POST,instance=getReferenceObject)
        #form = EnvironmentConfigForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            Env = Environment.objects.get(pk=1)
            if Env.storm == False:
                RoverMovementObj = RoverMovement.objects.get(pk=1)
                direction =  RoverMovementObj.direction
                RoverObj = RoverDesc.objects.get(pk=1)
                print("Battery level- "+str(RoverObj.battery))
                RoverObj.battery = RoverObj.battery-1
                BatteryStatus = RoverObj.battery
                #If the battery level goes to 1 after 10 successful movement it resets to 11
                if BatteryStatus == 1:
                    RoverObj.battery = 11
                print("New Battery level- " + str(RoverObj.battery))
                if direction == "up":
                    RoverObj.location_vertical += 1
                elif direction == "down":
                    RoverObj.location_vertical -= 1
                elif direction == "left":
                    RoverObj.location_horizontal -= 1
                elif direction == "right":
                    RoverObj.location_horizontal += 1
                if RoverObj.inventory_quantity == 0:
                    RoverObj.inventory_quantity=0
                else:
                    RoverObj.inventory_quantity -= 1
                RoverObj.save()
            # return Environment(request)
            #return HttpResponseRedirect(reverse(RoverStatus))
            return render(request, 'rover/RoverMove.html', {'form': form})
        else:
            print("Form is Invalid")
            return render(request, 'rover/RoverMove.html', {'form': form})
    else:
        #model= Environment()
        getReferenceObject = get_object_or_404(RoverMovement, pk=1)
        form = RoverMovementForm(instance=getReferenceObject)
        return render(request, 'rover/RoverMove.html', {'form': form})