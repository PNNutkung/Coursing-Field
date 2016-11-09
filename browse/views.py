from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mainmodels.models import Course, Category, FeaturedCourse, Transaction
# Create your views here.
def browseIndex(req):
    category = Category.objects.all()
    mostPopularCourses = Course.objects.raw('SELECT * FROM mainmodels_course as main_course JOIN (SELECT main_tran.courseID, COUNT(main_tran.takerID) as taker_amount FROM mainmodels_transaction as main_tran GROUP BY main_tran.courseID ORDER BY taker_amount DESC) as main_count ON main_course.courseID = main_count.courseID LIMIT 10;')
    bestRateCourses = Course.objects.raw('SELECT * FROM mainmodels_course as main_course JOIN (SELECT main_review.course_id, AVG(main_review.rating) as "average_rating" FROM mainmodels_review as main_review) as avg_main_review ON main_course.courseID = avg_main_review.course_id ORDER BY avg_main_review.average_rating DESC LIMIT 10;')
    featureCourses = FeaturedCourse.objects.raw('SELECT * FROM mainmodels_featuredcourse as main_feat JOIN mainmodels_course as main_course ON main_feat.course_id = main_course.courseID LIMIT 10;')
    return render(req, 'browse/index.html', {'pageTitle': 'Browse', 'categories': category, 'mostPopularCourses': mostPopularCourses, 'bestRateCourses': bestRateCourses, 'featureCourses':featureCourses})

def browseAll(req):
    '''Return the last courses.'''
    courseList = Course.objects.filter(isDelete=False, isPublish=True).order_by('-createdDate')
    browseFilter = 'All courses'
    return renderBrowse(req, courseList, browseFilter)

def renderBrowse(req, courseList, browseFilter):
    category = Category.objects.all()
    paginator = Paginator(courseList, 20)
    page = req.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    return render(req, 'browse/all.html', {'pageTitle': 'Browse courses', 'browseFilter': browseFilter,'courses': courses, 'pageRange': paginator.page_range, 'categories': category})

def browseCategory(req, categoryID):
    try:
        category = Category.objects.filter(categoryID=categoryID)
        browseFilter = category[0].categoryName
        courseList = Course.objects.filter(category=category, isDelete=False,  isPublish=True).order_by('-createdDate')
        return renderBrowse(req, courseList, browseFilter)
    except:
        return redirect(reverse('browse:browseIndex'))
