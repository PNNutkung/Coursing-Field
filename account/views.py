from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import django.contrib.auth as auth
from mainmodels.models import Profile, Course, Category
from django.urls import reverse
from datetime import datetime

# Create your views here.
def login(req):
    if req.user.is_authenticated:
        return redirect(reverse('index:index'))
    if req.method == 'POST':
        username = req.POST['_username']
        password = req.POST['_password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect(reverse('browse:browseIndex'))
    else:
        return render(req, 'account/login.html', {'pageTitle': 'Login'})

def register(req):
    return render(req, 'account/register.html')

def profile(req):
    teachingCourse = Course.objects.filter(owner=req.user)
    return render(req, 'account/profile.html')

def logout(req):
    auth.logout(req)
    return redirect(reverse('index:index'))
