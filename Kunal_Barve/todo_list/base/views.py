from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render ,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView ,DeleteView ,FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.conf import settings
from django.utils import timezone

from .models import Task
import requests


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        # Authenticate the user
        self.user = form.get_user()
        login(self.request, self.user)

        # Set cookies for the logged-in user
        response = super().form_valid(form)
        response.set_cookie('username', self.user.username)
        response.set_cookie('login_time', timezone.now().strftime('%Y-%m-%d %H:%M:%S'))

        # Add other cookie data as needed
        print("Cookies Set:", response.cookies)

        return response
    
    def  get_success_url(self):
        return reverse_lazy('tasks')
    
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    # once register directly login the user
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            # Send SMS notification
          
            mobile = self.request.POST.get('mobile')
            send_sms_notification(user.username, mobile)
            login(self.request ,user)
        return super(RegisterPage ,self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage ,self).get(*args, **kwargs)
    
# class RegisterPage(FormView):
#     template_name = 'base/register.html'
#     form_class = UserCreationForm
#     redirect_authenticated_user = True
#     success_url = reverse_lazy('tasks')

#     def form_valid(self, form):
#         # Save the user
#         user = form.save()

#         # Log the user in
#         login(self.request, user)

#         # Send SMS notification
#         country_code = self.request.POST.get('country_code')
#         mobile = self.request.POST.get('mobile')
#         if country_code and mobile:
#             send_sms_notification(user.username, country_code, mobile)

#         return super().form_valid(form)

#     def get(self, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return redirect('tasks')
#         return super(RegisterPage ,self).get(*args, **kwargs)

def send_sms_notification(username, mobile):
    # Format the phone number with the country code
   

    url = "https://us.sms.api.sinch.com/xms/v1/{}/batches".format(settings.SERVICE_PLAN_ID)
    payload = {
        "from": settings.SINCH_NUMBER,
        "to": [mobile],  # Use the formatted phone number
        "body": "Hello {}, you have successfully registered to the todo list app. Your username is {}.".format(username, username)
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(settings.API_TOKEN)
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    print(data)
class TaskList(LoginRequiredMixin ,ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        # we want the count of incomplete items
        context['count'] = context['tasks'].filter(complete = False).count()
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains = search_input)
            
        context['search_input'] = search_input
        return context
    def get(self, request, *args, **kwargs):
        # Access the logged-in user
        user = request.user
        
        # Print a debug statement to check if the view is being accessed
        print("TaskList view accessed by:", user.username)
        
        # Access cookies associated with the user
        user_cookies = request.COOKIES

        # Print the user's cookies if available
        if user_cookies:
            print(f"User: {user.username}, Cookies: {user_cookies}")
        else:
            print(f"No cookies found for user: {user.username}")

        # Call the parent class's get method
        return super().get(request, *args, **kwargs)

        
    
class TaskDetail(LoginRequiredMixin ,DetailView):
    model = Task
    context_object_name = "task"
    template_name =  'base/task.html'
    
class TaskCreate(LoginRequiredMixin ,CreateView):
    model = Task
    # we dont need user value
    fields = ["title" ,"description" ,"complete"]
    success_url = reverse_lazy('tasks')
    # this will make sure that user will create task in its own todo
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate ,self).form_valid(form)
    
    
class TaskUpdate(LoginRequiredMixin ,UpdateView):
    model = Task
    fields =["title" ,"description" ,"complete"]
    success_url = reverse_lazy('tasks')
    
class TaskDelete(LoginRequiredMixin ,DeleteView):
    model=Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')