from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from mainmodels.models import Category, Course
# Create your views here.
def createCourse(req):
    courseCategory = Category.objects.all()
    return render(req, 'course/createCourse.html', {'course_category':courseCategory})

def createNewCourse(req):
    if req.method is 'POST':
        courseName = req.POST['courseName']
        courseCategory = req.POST['courseCategory']
        courseDesc = req.POST['courseDesc']
        courseThumbnail = req.FILES['courseThumbnail']
        coursePrice = req.POST['coursePrice']
        #new_course =
        return redirect(reverse('course:createCourse'),{'errorMessage':'Create course successfully.'})
    else:
        return redirect(reverse('course:createCourse'),{'errorMessage':'Create course failed.'})
