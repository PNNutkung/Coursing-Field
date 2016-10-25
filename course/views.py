from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from mainmodels.models import Category
# Create your views here.
def createCourse(req):
    course_category = Category.objects.all()
    return render(req, 'course/createCourse.html', {'course_category':course_category})

def createNewCourse(req):
    return redirect(reverse('course:createCourse'))
