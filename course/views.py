from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
# Create your views here.
def createCourse(req):
    course_category = [{'value':1,'name':'Computer'},{'value':2,'name':'Art'}]
    return render(req, 'course/createCourse.html', {'course_category':course_category})

def createNewCourse(req):
    return redirect(reverse('course:createCourse'))
