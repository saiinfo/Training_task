from django.contrib import admin
from django.urls import path
from media_player import views
 
urlpatterns = [
    path('' , views.index , name = 'home'),
    path('clock' , views.clock , name = 'clock'),
    path('services' , views.services , name = 'services'),
]
