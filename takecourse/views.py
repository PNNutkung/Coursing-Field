from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from mainmodels.models import *
from django.http import HttpResponse

# Create your views here.
def take_course(request, courseID):
    if request.user.is_authenticated:
        course = Course.objects.get(courseID=courseID)
        userWithProfile = User.objects.get(id=request.user.id)
        newTransaction = Transaction(courseID=courseID, coursePrice=course.discountPrice, takerID=request.user.id, takerBalanceBeforePurchased=userWithProfile.profile.balance, usedCoupon=False)
        newTransaction.save()
        # new_takencourse = TakenCourse(course=course,taker=request.user)
        # new_takencourse.save()
        return redirect(reverse('watchvideo:show_contents_in_tabs',kwargs={'courseID' : courseID}))
    else:
        return redirect(reverse('mockaccount:index'))
