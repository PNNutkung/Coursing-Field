from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from mainmodels.models import *
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def show_content_in_tabs(request, courseID):
    if  request.user.is_authenticated:
        course = Course.objects.get(courseID=courseID)
        if hasTakenCourse(request.user.id, courseID):
            # course = Course.objects.get(courseID=courseID)
            videos = Video.objects.filter(course=course,isDelete=False)
            # preview = CoursePreview.objects.get(course=course,isDelete=False)
            courseInCategory = course.category.categoryName
            # courseInCategory = courseInCategory.objects.get(course=course)
            commentsList = []
            for video in videos:
                commentsOfVideo = Comment.objects.filter(video=video, isDelete=False)
                commentsList.append(commentsOfVideo)
            print("Comments #",len(commentsList))
            lecturesList = [{'video' : t[0], 'comments' : t[1]} for t in zip (videos,commentsList)]
            return render(request, 
                'watchvideo/show_content_in_tabs.html', 
                {'course' : course, 'videos' : videos, 'courseInCategory' : courseInCategory, 'lecturesList' : lecturesList}
            )
        else:
            return HttpResponse('Redirect to purchase page')
    else:
        return redirect(reverse('mockaccount:index'))

def hasTakenCourse(userID,courseID):
    try:
        transaction = Transaction.objects.get(courseID=courseID, takerID=userID)
        if transaction is not None:
            return True
    except ObjectDoesNotExist:
        return False