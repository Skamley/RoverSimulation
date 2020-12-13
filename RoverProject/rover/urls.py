from django.conf.urls import url
from rover import views
app_name='rover'

urlpatterns=[
    #url(r'$^',views.index, name='index'),
    url(r'environment/configuration/', views.EnvironmentConfiguration, name="EnvironmentConfiguration"),
    url(r'environment/', views.EnvironmentUpdate, name="EnvironmentUpdate"),
    url(r'rover/configuration/', views.RoverConfiguration, name='RoverConfiguration'),
    url(r'rover/status', views.RoverStatus, name='RoverStatus'),
    url(r'rover/move/', views.RoverMove, name='RoverMove'),
]
