from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import django.contrib.auth as auth
from mainmodels.models import Profile, Course, Category
from django.urls import reverse
from datetime import datetime
import re

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
    if req.method == 'POST':
        try:
            username = req.POST['username']
            password = req.POST['password']
            firstname = req.POST.get('firstname')
            lastname = req.POST.get('lastname')
            email = req.POST.get('email')
            gender = req.POST.get('gender', 'M')
            profilePicture = req.FILES.get('profilepicture')
            birthDate_str = req.POST.get('birthday')
            birthDate = datetime.strptime(birthDate_str, '%Y-%m-%d').date()
            user = User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
            user.profile.gender = gender[0]
            user.profile.profilePicture = profilePicture
            user.profile.birthDate = birthDate
            user.save()
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(req, user)
                return redirect(reverse('account:profile'))
        except IntegrityError:
            return render(req, 'account/register.html', {'message': 'This username has  already taken.'})
    else:
        return render(req, 'account/register.html')

def profile(req):
    #teachingCourse = Course.objects.filter(owner=req.user)
    return render(req, 'account/profile.html')

def logout(req):
    auth.logout(req)
    return redirect(reverse('index:index'))
