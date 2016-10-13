from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(req):
    return HttpResponse('Hello, World.')
