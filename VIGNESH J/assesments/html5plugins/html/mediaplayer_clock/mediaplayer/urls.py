from django.urls import path
from . import views

urlpatterns = [
    path('mediaplayer/', views.media_player, name='media_player'),
    path('clock/', views.clock, name='clock'),
]
