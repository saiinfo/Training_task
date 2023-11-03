from django.shortcuts import render , HttpResponse

def index(request):
    return render(request,'vedio.html')
 
def clock(request):
    return render(request ,'clock.html')

def services(request):
    return HttpResponse('this is services')
 