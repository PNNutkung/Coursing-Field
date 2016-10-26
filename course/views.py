from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from mainmodels.models import Category, Course, CourseInCategory, TakenCourse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def createCourse(req):
    if not req.user.is_authenticated:
        return redirect(reverse('mockaccount:index'))
    else:
        if req.method == 'POST':
            try:
                courseName = req.POST['courseName']
                courseCategory = req.POST['courseCategory']
                courseDesc = req.POST['courseDesc']
                courseThumbnail = req.FILES['courseThumbnail']
                coursePrice = req.POST['coursePrice']
                owner = req.user

                newCourse = Course(courseName=courseName, courseDesc=courseDesc,courseThumbnail=courseThumbnail, owner=owner, coursePrice=coursePrice, isDelete=False)
                newCourse.save()

                category = Category.objects.get(categoryID=courseCategory)
                newCourseCategory = CourseInCategory(category=category, course=newCourse)
                newCourseCategory.save()

                return render(req, 'course/createCourse.html', {'courseCategory':courseCategory, 'success': True, 'message': 'Create course successfully.'})
            except:
                return render(req, 'course/createCourse.html', {'courseCategory':courseCategory, 'success': False, 'message': 'Create course failed.'})
        else:
            courseCategory = Category.objects.all()
            return render(req, 'course/createCourse.html', {'courseCategory':courseCategory})

def view_course(req, courseID):
    if req.user.is_authenticated:
        course = Course.objects.get(courseID=courseID)
        hasTakencourse = False
        try:
            takenCourse = TakenCourse.objects.get(course=course,taker=req.user)
            if takenCourse is not None:
                hasTakencourse = True
        except ObjectDoesNotExist:
            hasTakencourse = False
        userWithProfile = User.objects.get(id=req.user.id)
        inCategory = CourseInCategory.objects.get(course=course).category.categoryName
        leftBalance = int(userWithProfile.profile.balance - course.coursePrice)
        return render(req, 'course/viewCourse.html', {'course' : course, 'hasTakenCourse' : hasTakencourse, 'inCategory' : inCategory, 'userWithProfile' : userWithProfile, 'leftBalance': leftBalance})
    else:
        return redirect(reverse('mockaccount:index'))
