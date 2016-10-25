from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from mainmodels.models import *

# Create your views here.
def show_content_in_tabs(request, courseID):
    course = get_object_or_404(Course, courseID=courseID)
    # course = Course.objects.get(courseID=courseID)
    videos = Video.objects.get(course=course)
    preview = CoursePreview.objects.get(course=course)
    courseInCategory = get_object_or_404(CourseInCategory, course=course)
    # courseInCategory = courseInCategory.objects.get(course=course)
    return render(request, 
        'watchvideo/show_content_in_tabs.html', 
        {'course' : course, 'videos' : videos, 'preview' : preview, 'courseInCategory' : courseInCategory}
    )
