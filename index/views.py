from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
# Create your views here.
def index(req):
    return render(req, 'index/main.html', {'pageTitle': 'Coursing Field'})
