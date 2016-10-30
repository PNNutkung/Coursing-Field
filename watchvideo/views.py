from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from mainmodels.models import *
from django.http import HttpResponse

# Create your views here.
def show_content_in_tabs(request, courseID):
    if  request.user.is_authenticated:
        course = get_object_or_404(Course, courseID=courseID)
        if hasTakenCourse(request.user, course):
            # course = Course.objects.get(courseID=courseID)
            videos = Video.objects.filter(course=course,isDelete=False)
            preview = CoursePreview.objects.get(course=course,isDelete=False)
            courseInCategory = get_object_or_404(CourseInCategory, course=course)
            # courseInCategory = courseInCategory.objects.get(course=course)
            commentsList = []
            for video in videos:
                commentsOfVideo = Comment.objects.filter(video=video,isDelete=False)
                commentsList.append(commentsOfVideo)
            lecturesList = [{'video' : t[0], 'comments' : t[1]} for t in zip (videos,commentsList)]
            return render(request, 
                'watchvideo/show_content_in_tabs.html', 
                {'course' : course, 'videos' : videos, 'preview' : preview, 'courseInCategory' : courseInCategory, 'lecturesList' : lecturesList}
            )
        else:
            return HttpResponse('Redirect to purchase page')
    else:
        return redirect(reverse('mockaccount:index'))

def hasTakenCourse(user,course):
    takenCourse = TakenCourse.objects.get(course=course,taker=user)
    if takenCourse is not None:
        return True
    else:
        return False