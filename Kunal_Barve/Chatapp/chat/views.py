from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chatPage.html", context)



def check_session_expiration(request):
    if not request.user.is_authenticated:
        return JsonResponse({'status': 'expired'}, status=401)
    else:
        return JsonResponse({'status': 'active'})

