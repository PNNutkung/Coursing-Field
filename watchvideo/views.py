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
            orderVideosInCourse = OrderVideoInCourse.objects.filter(course=course).order_by('orderNo')
            # courseInCategory = courseInCategory.objects.get(course=course)
            commentsList = []
            orderNoList = []
            orderNo = 1
            # for video in videos:
            #     commentsOfVideo = Comment.objects.filter(video=video, isDelete=False)
            #     commentsList.append(commentsOfVideo)
            for orderVideoInCourse in orderVideosInCourse:
                commentsOfVideo = Comment.objects.filter(video=orderVideoInCourse.video, isDelete=False)
                commentsList.append(commentsOfVideo)
                orderNoList.append(orderNo)
            # print("Comments #",len(commentsList))
            # lecturesList = [{'video' : t[0], 'comments' : t[1]} for t in zip (videos,commentsList)]
            lecturesList = [{'orderVideoInCourse' : t[0], 'comments' : t[1]} for t in zip (orderVideosInCourse,commentsList)]
            return render(request, 
                'watchvideo/show_content_in_tabs.html', 
                {'course' : course, 'videos' : videos, 'courseInCategory' : courseInCategory, 'lecturesList' : lecturesList}
            )
        else:
            return HttpResponse('Redirect to purchase page')
    else:
        return redirect(reverse('mockaccount:index'))

def overview(request, courseID):
    if request.user.is_authenticated:
        course = Course.objects.select_related('owner').get(courseID=courseID)
        orderVideos = OrderVideoInCourse.objects.select_related('video').filter(course=course).order_by('orderNo')
        if request.user.id == course.owner_id:
            return redirect(reverse('course:manage_course_overview', kwargs={ 'courseID' : courseID}))
        elif hasTakenCourse(request.user.id, courseID):
            return render(request, 'watchvideo/tabs_with_content.html', { 'isOwner' : False, 'isOverview' : True, 'course' : course, 'orderVideos' : orderVideos })
        else:
            return redirect(reverse('course:view_course', kwargs={ 'courseID' : courseID}))
    return redirect(reverse('account:login'))

def video_tab(request, courseID, videoID):
    if request.user.is_authenticated:
        course = Course.objects.select_related('owner').get(courseID=courseID)
        if request.user.id == course.owner_id:
            return redirect(reverse('course:manage_course_overview', kwargs={ 'courseID' : courseID}))
        elif hasTakenCourse(request.user.id, courseID):
            video = Video.objects.select_related('course').get(videoID=videoID)
            comments = Comment.objects.select_related('owner').filter(video=video)
            orderVideos = OrderVideoInCourse.objects.select_related('video').filter(course=video.course).order_by('orderNo')
            return render(request, 'watchvideo/tabs_with_content.html', { 'isOwner' : False, 'isVideoTab' : True, 'course' : course, 'video' : video, 'comments' : comments, 'orderVideos' : orderVideos })
        else:
            return redirect(reverse('course:view_course', kwargs={ 'courseID' : courseID}))
    return redirect(reverse('account:login'))
    
def hasTakenCourse(userID,courseID):
    try:
        transaction = Transaction.objects.get(courseID=courseID, takerID=userID)
        if transaction is not None:
            return True
    except ObjectDoesNotExist:
        return False