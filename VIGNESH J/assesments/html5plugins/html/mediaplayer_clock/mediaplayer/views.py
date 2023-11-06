from django.shortcuts import render

def media_player(request):
    return render(request, 'mediaplayer/mediaplayer.html')

def clock(request):
    return render(request, 'mediaplayer/clock.html')
