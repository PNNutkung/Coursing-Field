from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from mainmodels.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Avg
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
        isOwner = False
        if req.user.id == course.owner.id:
            isOwner = True
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

        numberOfLectures = Video.objects.filter(course=course).count()

        reviewList = Review.objects.filter(course=course).order_by('-reviewDate')
        reviewPaginator = Paginator(reviewList, 5)
        page = req.GET.get('reviewPage')
        try:
            reviews = reviewPaginator.page(page)
        except PageNotAnInteger:
            reviews = reviewPaginator.page(1)
        except EmptyPage:
            reviews = reviewPaginator.page(paginator.num_pages)

        try:
            averageRating = Review.objects.filter(course=course).aggregate(Avg('rating'))
        except:
            averageRating = 0

        reviewsCount = Review.objects.filter(course=course).count()

        try:
            fiveStarRate = {'star':'5 Stars','percentage':int(float(Review.objects.filter(course=course,rating=5).count()/reviewsCount)*100)}

            fourStarRate = {'star':'4 Stars','percentage':int(float(Review.objects.filter(course=course,rating=4).count()/reviewsCount)*100)}

            threeStarRate = {'star':'3 Stars','percentage':int(float(Review.objects.filter(course=course,rating=3).count()/reviewsCount)*100)}

            twoStarRate = {'star':'2 Stars','percentage':int(float(Review.objects.filter(course=course,rating=2).count()/reviewsCount)*100)}

            oneStarRate = {'star':'1 Star','percentage':int(float(Review.objects.filter(course=course,rating=1).count()/reviewsCount)*100)}

            reviewRateLevel = [fiveStarRate, fourStarRate, threeStarRate, twoStarRate, oneStarRate]
        except:
            reviewRateLevel = []

        return render(req, 'course/viewCourse.html', {'course' : course, 'hasTakenCourse' : hasTakencourse, 'inCategory' : inCategory, 'userWithProfile' : userWithProfile, 'leftBalance': leftBalance,'numberOfLectures':numberOfLectures, 'reviews':reviews, 'averageRating': averageRating,'reviewRateLevel':reviewRateLevel,})
    else:
        return redirect(reverse('mockaccount:index'))

def manage_course(req, courseID):
    if req.user.is_authenticated:
        course = Course.objects.get(courseID=courseID)
        videos = Video.objects.filter(course=course)
        inCategory = CourseInCategory.objects.get(course=course).category.categoryName
        isOwner = False
        if req.user.id == course.owner.id:
            isOwner = True
        else:
            return redirect(reverse('course:view_course'))
        return render(req, 'watchvideo/show_content_in_tabs.html',{ 'course' : course, 'videos' : videos, 'isOwner' : isOwner, 'inCategory' : inCategory })
    else:
        return redirect(reverse('mockaccount:index'))

def edited_course(req, courseID):
    if req.method == 'POST':
        course = Course.objects.get(courseID=courseID)
        newCourseName = req.POST.get('courseName')
        if newCourseName is not None:
            course.courseName = newCourseName
        # Missing Category might have to delete old one before insert new CourseInCategory
        newPreviewVideo = req.FILES.get('previewVideo')
        if newPreviewVideo is not None:
            try:
                #Assume there is only one preview video. Any old ones should be labeled isDelete=True
                coursePreview = CoursePreview.objects.get(course=course,isDelete=False)
                #Add for loop to set old preview videos as isDelete=True
                coursePreview.isDelete = True
                coursePreview.save()
            except ObjectDoesNotExist:
                print("Object does not exist creating new one")
            finally:
                newCoursePreview = CoursePreview(course=course,previewVideo=newPreviewVideo,isDelete=False)
                newCoursePreview.save()
        newCourseThumbnail = req.FILES.get('courseThumbnail')
        if newCourseThumbnail is not None:
            course.courseThumbnail = newCourseThumbnail
        newCourseDesc = req.POST.get('courseDesc')
        if newCourseDesc is not None:
            course.courseDesc = newCourseDesc
        course.save()
        return redirect(reverse('course:manage_course', kwargs={'courseID' : courseID }))
    else:
        return HttpResponse('Failed to post.')

def upload_video(req, courseID):
    if req.method == 'POST':
        videoName = req.POST['videoName']
        videoFile = req.FILES['videoToUpload']
        course = Course.objects.get(courseID=courseID)
        new_video = Video(videoName=videoName,videoFile=videoFile,course=course,isDelete=False)
        new_video.save()
        return redirect(reverse('course:manage_course', kwargs={'courseID' : courseID }))
    else:
        return HttpResponse('Failed to post.')

def reviewCourse(req, courseID):
    if req.method == 'POST':
        course = Course.objects.get(courseID=courseID)
        reviewDesc = req.POST['reviewDesc']
        reviewRate = req.POST['reviewRating']
        newReview = Review(reviewDesc=reviewDesc, owner=req.user, course=course, rating=reviewRate, isDelete=False)
        newReview.save()
    return redirect(reverse('course:view_course', kwargs={'courseID': courseID}))

def comment_on_video(req, courseID, videoID):
    if req.method == 'POST':
        commentDesc = req.POST.get('commentDesc','')
        video = Video.objects.get(videoID=videoID)
        comment = Comment(owner=req.user,video=video,commentDesc=commentDesc,isDelete=False)
        comment.save()
        print( comment.commentDesc )
        if req.user.id == courseID:
            return redirect(reverse('course:manage_course', kwargs={'courseID' : courseID } ))
        else:
            return redirect(reverse('watchvideo:show_contents_in_tabs', kwargs={'courseID' : courseID } ))
    else:
        return HttpResponse('Failed to post.')