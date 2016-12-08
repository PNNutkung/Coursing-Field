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
        return redirect(reverse('index:index'))
    else:
        if req.method == 'POST':
            # try:
            courseName = req.POST['courseName']
            courseCategory = req.POST['courseCategory']
            courseShortDesc = req.POST['courseDesc']
            # if courseThumbnail is None:
            #     dummyCourse = Course.objects.get(courseID="11")
            #     courseThumbnail = dummyCourse.courseThumbnail
            coursePrice = req.POST['coursePrice']
            owner = req.user
            category = Category.objects.get(categoryID=courseCategory)
            newCourse = Course(courseName=courseName, courseShortDesc=courseShortDesc, owner=owner, coursePrice=coursePrice, isDelete=False, isPublish=False, category=category, discountPercentage=0, discountPrice=coursePrice)
            newCourse.save()

            return render(req, 'course/createCourse.html', {'courseCategory':courseCategory, 'success': True, 'message': 'Create course successfully.'})
            # except:
            #     return render(req, 'course/createCourse.html', {'courseCategory':courseCategory, 'success': False, 'message': 'Create course failed.'})
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
            transaction = Transaction.objects.get(courseID=courseID, takerID=req.user.id)
            # takenCourse = TakenCourse.objects.get(course=course,taker=req.user)
            if transaction is not None:
                hasTakencourse = True
        except ObjectDoesNotExist:
            hasTakencourse = False
        userWithProfile = User.objects.get(id=req.user.id)
        inCategory = course.category.categoryName
        if course.discountPercentage > 0:
            leftBalance = int(userWithProfile.profile.balance - course.coursePrice)
        else:
            leftBalance = int(userWithProfile.profile.balance - course.discountPrice)
        canTakeCourse = False
        if leftBalance >= 0:
            canTakeCourse = True
        numberOfLectures = Video.objects.filter(course=course).count()
        reviewList = Review.objects.filter(course=course).order_by('-reviewedDate')
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

        return render(req, 'course/viewCourse.html', {'course' : course, 'hasTakenCourse' : hasTakencourse, 'inCategory' : inCategory, 'userWithProfile' : userWithProfile, 'leftBalance': leftBalance,'numberOfLectures':numberOfLectures, 'reviews':reviews, 'averageRating': averageRating,'reviewRateLevel':reviewRateLevel, 'isOwner' : isOwner, 'canTakeCourse': canTakeCourse, })
    else:
        return redirect(reverse('index:index'))

def manage_course(req, courseID):
    if req.user.is_authenticated:
        course = Course.objects.get(courseID=courseID)
        isOwner = False
        if req.user.id == course.owner_id:
            isOwner = True
        else:
            return redirect(reverse('course:view_course'))
        orderVideosInCourse = OrderVideoInCourse.objects.filter(course=course,orderNo__gte=1).select_related('video').order_by('orderNo')
        commentsList = []
        nextAndPrevVideosIDList = []
        inCategory = course.category.categoryName
        categories = Category.objects.all()
        orderNoList = []
        orderNo = 0
        currentIndex = 0
        lastIndex = orderVideosInCourse.count() - 1
        for orderVideoInCourse in orderVideosInCourse:
            orderNo += 1
            commentsOfVideo = Comment.objects.filter(video=orderVideoInCourse.video, isDelete=False)
            prevIndex = currentIndex - 1
            nextIndex = currentIndex + 1
            if prevIndex >= 0 and nextIndex <= lastIndex:
                next_prev = (orderVideosInCourse[currentIndex - 1].video_id, orderVideosInCourse[currentIndex + 1].video_id)
            elif prevIndex < 0:
                if currentIndex + 1 <= orderVideosInCourse.count():
                    next_prev = (None, orderVideosInCourse[currentIndex].video_id)
                else: next_prev = (None, None)
            else:
                next_prev = (orderVideosInCourse[currentIndex - 1].video_id, None)
            # print(next_prev)
            nextAndPrevVideosIDList.append(next_prev)
            commentsList.append(commentsOfVideo)
            orderNoList.append(orderNo)
            currentIndex += 1
        # lecturesList = [{'video' : t[0], 'comments' : t[1]} for t in zip (videos,commentsList)]
        lecturesList = [{'orderVideoInCourse' : t[0], 'comments' : t[1], 'nextAndPrev' : t[2]} for t in zip (orderVideosInCourse,commentsList,nextAndPrevVideosIDList)]
        return render(req, 'watchvideo/show_content_in_tabs.html',{ 'course' : course, 'lecturesList' : lecturesList, 'isOwner' : isOwner, 'inCategory' : inCategory, 'categories' : categories, 'orderNoList' : orderNoList, 'orderVideosInCourse' : orderVideosInCourse })
    else:
        return redirect(reverse('index:index'))

def manage_course_overview(req, courseID):
    if req.user.is_authenticated:
        course = Course.objects.select_related('owner').get(courseID=courseID)
        if req.user.id == course.owner_id:
            # isOwner = True
            # isOverview = True
            orderVideos = OrderVideoInCourse.objects.select_related('video').filter(course=course, orderNo__gte=1).order_by('orderNo')
            categories = Category.objects.all()
            orderNoList = []
            # orderNo = 0
            for orderVideo in orderVideos:
                orderNoList.append(orderVideo.orderNo)
            # tabsList = orderVideos.values('video')
            return render(req, 'watchvideo/tabs_with_content.html', { 'isOverview' : True, 'isOwner' : True, 'categories' : categories, 'orderNoList' : orderNoList, 'orderVideos' : orderVideos, 'course' : course })
    else:
        return redirect(reverse('course:view_course'))

def manage_course_by_video_id(req, courseID, videoID):
    if req.user.is_authenticated:
        # course = Course.objects.get(courseID=courseID)
        video = Video.objects.select_related('course').get(videoID=videoID)
        orderVideos = OrderVideoInCourse.objects.select_related('video').filter(course=video.course, orderNo__gte=1).order_by('orderNo')
        comments = Comment.objects.select_related('owner').filter(video=video)
        lastVideoOrder = orderVideos.reverse()[0].orderNo
        if req.user.id == video.course.owner_id:
            return render(req, 'watchvideo/tabs_with_content.html', { 'isVideoTab' : True, 'isOwner' : True, 'video' : video, 'orderVideos' : orderVideos, 'course' : video.course, 'comments' : comments, 'lastVideoOrder' : lastVideoOrder})
    else:
        return redirect(reverse('course:view_course'))

def edited_course(req, courseID):
    if req.method == 'POST':
        course = Course.objects.get(courseID=courseID)
        newCourseName = req.POST.get('courseName')
        if len(newCourseName) > 0:
            course.courseName = newCourseName
        newCategoryID = req.POST.get('courseCategory')
        if len(newCategoryID) > 0:
            try:
                category = Category.objects.get(categoryID=newCategoryID)
                course.category = category
            except ObjectDoesNotExist:
                print("Object does not exist")
        newPreviewVideo = req.FILES.get('previewVideo',None)
        if newPreviewVideo is not None:
            course.previewVideoFile = newPreviewVideo
        newCourseThumbnail = req.FILES.get('courseThumbnail')
        if newCourseThumbnail is not None:
            course.courseThumbnail = newCourseThumbnail
        newCourseFullDesc = req.POST.get('courseFullDesc')
        if len(newCourseFullDesc) > 0:
            course.courseFullDesc = newCourseFullDesc
        newCourseShortDesc = req.POST.get('courseShortDesc')
        if len(newCourseShortDesc) > 0:
            course.courseShortDesc = newCourseShortDesc
        isPublish = req.POST.get('isPublish')
        if isPublish is not None:
            course.isPublish = True
            # print('New value of isPublish', 'True')
        else:
            course.isPublish = False
            print('New value of isPublish', 'False')
        newDiscountPercentage_str = req.POST.get('discountPercentage')
        if len(newDiscountPercentage_str) > 0:
            newDiscountPercentage = int(newDiscountPercentage_str)
            course.discountPercentage = newDiscountPercentage
            if newDiscountPercentage > 0:
                print('New value of discountPercentage', newDiscountPercentage)
                newDiscountPrice = course.coursePrice * ( 100 - newDiscountPercentage ) / 100
                print('new value of discountPrice', newDiscountPrice)
                course.discountPrice = newDiscountPrice
            else:
                print('New value of discountPercentage', newDiscountPercentage)
                newDiscountPrice = course.coursePrice
                print('new value of discountPrice', newDiscountPrice)
        course.save()
        return redirect(reverse('course:manage_course', kwargs={'courseID' : courseID }))
    else:
        return HttpResponse('Failed to post.')

def upload_video(req, courseID):
    if req.method == 'POST':
        videoName = req.POST.get('videoName')
        videoFile = req.FILES['videoToUpload']
        videoDesc = req.POST.get('videoDesc')
        course = Course.objects.get(courseID=courseID)
        new_video = Video(videoName=videoName,videoFile=videoFile,course=course,videoDesc=videoDesc,isDelete=False)
        new_video.save()
        course = Course.objects.get(courseID=courseID)
        newOrderNo = OrderVideoInCourse.objects.filter(course=course,orderNo__gte=1).count() + 1
        newOrderVideoInCourse = OrderVideoInCourse(course=course, video=new_video, orderNo=newOrderNo)
        newOrderVideoInCourse.save()
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

def edited_video(req, courseID, videoID):
    if req.method == 'POST':
        course = Course.objects.get(courseID=courseID)
        video = Video.objects.get(videoID=videoID)
        editedOrderVideoInCourse = OrderVideoInCourse.objects.get(course=course, video=video)
        newVideoName = req.POST.get('videoName')
        newVideoFile = req.POST.get('videoFile')
        newVideoDesc = req.POST.get('videoDesc')
        if newVideoFile is not None:
            newVideo = Video(course=course,videoFile=newVideoFile)
            if len(newVideoName) > 0:
                newVideo.videoName = newVideoName
            else:
                newVideo.videoName = video.videoName
            if len(newVideoDesc) > 0:
                newVideo.videoDesc = newVideoDesc
            else:
                newVideo.videoDesc = video.videoDesc
            newVideo.save()
            video.isDelete = True
            video.save()
            editedOrderVideoInCourse.video = newVideo
            editedOrderVideoInCourse.save()
        else:
            if len(newVideoName) > 0:
                video.videoName = newVideoName
            else:
                video.videoName = video.videoName
            if len(newVideoDesc) > 0:
                video.videoDesc = newVideoDesc
            else:
                video.videoDesc = video.videoDesc
            video.save()

    return redirect(reverse('course:manage_course', kwargs={'courseID' : courseID } ))

def reordered_video(req, courseID):
    if req.method == 'POST':
        course = Course.objects.get(courseID=courseID)
        videos = Video.objects.filter(course=course, isDelete=False)
        lastVideoOrderNo = OrderVideoInCourse.objects.filter(course=course).count()
        for video in videos:
            newOrderNo = int(req.POST.get(str(video.videoID),lastVideoOrderNo + 1))
            reorderedVideo = OrderVideoInCourse.objects.get(course=course,video=video)
            print('Old order#',reorderedVideo.orderNo, 'of', reorderedVideo.video.videoName)
            reorderedVideo.orderNo = newOrderNo
            print('New order#', reorderedVideo.orderNo, 'of', reorderedVideo.video.videoName)
            reorderedVideo.save()
    return redirect(reverse('course:manage_course', kwargs={'courseID' : courseID } ))

def remove_video(req, courseID, videoID):
    if req.method == 'POST':
        course = Course.objects.get(courseID=courseID)
        video = Video.objects.get(videoID=videoID)
        videoNameToDelete = req.POST.get('confirmToDelete','')
        if videoNameToDelete == video.videoName:
            video.isDelete = True
            orderVideo = OrderVideoInCourse.objects.get(course=course, video=video)
            greaterOrderNoVideos = OrderVideoInCourse.objects.filter(course=course, orderNo__gt=orderVideo.orderNo)
            greaterOrderNoVideos.update(orderNo=F('orderNo') - 1)
            # orderVideo.update(orderNo=-1)
            orderVideo.orderNo = -1
            ordervideo.save()

    return redirect(reverse('course:manage_course', kwargs={'courseID' : courseID}))
