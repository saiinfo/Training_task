from django.shortcuts import render , HttpResponse

def index(request):
    context = {
        'variable' : 'this i sent'
    }
    return render(request , 'index.html' , context)

def vedio(request):
    return render(request,'vedio.html' )
 
def clock(request):
    return render(request ,'clock.html')

# def services(request):
#     context = {
#         'variable' : 'this i sent'
#     }
#     return render(request , 'services.html' , context)

# def services(request):
#     return HttpResponse('this is services')
 