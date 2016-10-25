from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from mainmodels.models import Category, Course, CourseInCategory
from django.contrib.auth.models import User
# Create your views here.
def createCourse(req):
    courseCategory = Category.objects.all()
    return render(req, 'course/createCourse.html', {'courseCategory':courseCategory})

def createNewCourse(req):
    if req.method == 'POST':
        courseName = req.POST['courseName']
        courseCategory = req.POST['courseCategory']
        courseDesc = req.POST['courseDesc']
        courseThumbnail = req.FILES['courseThumbnail']
        coursePrice = req.POST['coursePrice']
        owner = User.objects.get(username='nut')

        newCourse = Course(courseName=courseName, courseDesc=courseDesc,courseThumbnail=courseThumbnail, owner=owner, coursePrice=coursePrice, isDelete=False)
        newCourse.save()

        category = Category.objects.get(categoryID=courseCategory)
        newCourseCategory = CourseInCategory(category=category, course=newCourse)
        newCourseCategory.save()
        return redirect(reverse('course:createCourse'),{'errorMessage':'Create course successfully.'})
    else:
        return redirect(reverse('course:createCourse'),{'errorMessage':'Create course failed.'})
