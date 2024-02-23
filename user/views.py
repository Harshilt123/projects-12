from typing import Any
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import User
from .forms import UserRegistrationForm 
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView

class UserRegisterView(CreateView):
    template_name = 'user/user_register.html'
    model = User
    form_class = UserRegistrationForm
    success_url = '/user/login/'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        if self.send_mail(email):
            return super().form_valid(form)
        else:
            return super().form_valid(form)

    def send_mail(self, to):
        subject = 'Welcome to EXPENSE'
        message = 'Hope you are enjoying our website'
        recepientList = [to]
        EMAIL_FROM = settings.EMAIL_HOST_USER
        send_mail(subject, message, EMAIL_FROM, recepientList)
        return True

class UserLoginView(LoginView): 
    template_name = 'user/login.html'
    model = User
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_user:
                return '/user/user_dashboard/'

class UserDashboardView(ListView):
    template_name = 'user/user_dashboard.html'
