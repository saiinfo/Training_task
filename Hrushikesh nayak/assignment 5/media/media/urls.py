from django.contrib import admin
from django.urls import path
from media_player import views
 
urlpatterns = [
    path('' , views.index , name = 'home'),
    path('time' , views.clock , name = 'time'),
    path('vedio' , views.vedio , name = 'services'),
]
