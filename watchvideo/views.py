from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from mainmodels.models import *

# Create your views here.
def show_content_in_tabs(request, courseID):
    course = Course.objects.get(courseID=courseID)
    videos = Video.objects.get(course=course)
    return render(request, 
        'watchvideo/show_content_in_tabs.html', 
        {'course' : course, 'videos' : videos}
    )
