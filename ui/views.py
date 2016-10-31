from django.http import Http404
from django.shortcuts import render, get_object_or_404
#from django.template import loader

def index(request):
    return render(request , 'ui/index.html')

def view(request):
    return render(request , 'ui/view_course.html')

def browse(request):
    return render(request , 'ui/browse_course.html')

def register(request):
    return render(request , 'ui/register.html')

def create(request):
    return render(request , 'ui/create.html')
