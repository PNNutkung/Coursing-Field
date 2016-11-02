from django.shortcuts import render
from django.urls import reverse
from mainmodels.models import Course, Category

# Create your views here.
def login(req):
    return render(req, 'account/login.html')

def register(req):
    return render(req, 'account/register.html')

def profile(req):
    teachingCourse = Course.objects.filter(owner=req.user)
    return render(req, 'account/profile.html')
