from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
import re

# Create your views here.
def index(req):
    return render(req,'login/login.html')


def do_login(req):
    username = req.POST['username']
    password = req.POST['password']
    #return  redirect('login/profile/'+username)
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(req, user)
        return  HttpResponseRedirect('/login/profile/')
    else:
        return HttpResponseRedirect('/login/', { 'error_message': 'Invalid username or password'})


def register(req):
    return render(req, 'login/register.html')

def create_new_user(req):
    firstname = req.POST['firstname']
    lastname = req.POST['lastname']
    username = req.POST['username']
    password = req.POST['password']
    confirm_password = req.POST['confirm_password']
    bday = req.POST['bday']
    gender = req.POST['gender']
    user = None

    try:
        user = User.objects.get(username=username)
    except(User.DoesNotExist):
        if user is not None:
            return render(req, 'login/register.html', {
                'error_message': 'This username has already taken.'
            })
        elif password != confirm_password:
            return render(req, 'login/register.html', {
                'error_message': 'Your password is not match.'
            })
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', username):
            return render(req, 'login/register.html', {
                'error_message': 'Your email is not valid.'
            })
        else:
            user = User.objects.create_user(username, email=username, password=password, first_name=firstname, last_name=lastname)
            return render(req, 'login/login.html', {
                'error_message': 'Register successfully.'
            })

def profile(req):
    user = req.user
    return render(req, 'login/user_profile.html', {'user':user})
