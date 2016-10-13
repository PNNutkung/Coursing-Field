from django.shortcuts import render, redirect, get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
def index(req):
    return render(req, 'browse/index.html')
