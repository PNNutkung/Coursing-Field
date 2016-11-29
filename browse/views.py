from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mainmodels.models import Course, Category, FeaturedCourse, Transaction
# Create your views here.
def browseIndex(req):
    categories = Category.objects.all()
    mostPopularCourses = Course.objects.raw('SELECT * FROM mainmodels_course as main_course JOIN (SELECT main_tran.courseID, COUNT(main_tran.takerID) as taker_amount FROM mainmodels_transaction as main_tran GROUP BY main_tran.courseID ORDER BY taker_amount DESC) as main_count ON main_course.courseID = main_count.courseID LIMIT 10;')
    bestRateCourses = Course.objects.raw('SELECT * FROM mainmodels_course as main_course JOIN (SELECT main_review.course_id, AVG(main_review.rating) as "average_rating" FROM mainmodels_review as main_review) as avg_main_review ON main_course.courseID = avg_main_review.course_id ORDER BY avg_main_review.average_rating DESC LIMIT 10;')
    featureCourses = FeaturedCourse.objects.raw('SELECT * FROM mainmodels_featuredcourse as main_feat JOIN mainmodels_course as main_course ON main_feat.course_id = main_course.courseID LIMIT 10;')
    return render(req, 'browse/index.html', {'pageTitle': 'Browse', 'categories': categories, 'mostPopularCourses': mostPopularCourses, 'bestRateCourses': bestRateCourses, 'featureCourses':featureCourses})

def browseAll(req):
    '''Return the last courses.'''
    categories = Category.objects.all()
    courses = Course.objects.filter(isDelete=False, isPublish=True).order_by('-createdDate')
    browseFilter = 'All courses'
    # return renderBrowse(req, courseList, browseFilter)
    return render(req, 'browse/all.html', {'pageTitle': 'All courses', 'browseFilter' : browseFilter, 'categories' : categories, 'courses' : courses })

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
    return render(req, 'browse/all.html', {'pageTitle': 'Browse courses', 'browseFilter': browseFilter, 'courses': courses, 'pageRange': paginator.page_range, 'categories': category})

def browseCategory(req, categoryID):
    # try:
    categories = Category.objects.all()
    category = Category.objects.get(categoryID=categoryID)
    browseFilter = category.categoryName
    # courseList = Course.objects.filter(category=category, isDelete=False,  isPublish=True).order_by('-createdDate')
    mostPopularCourses = Course.objects.raw('SELECT * FROM mainmodels_course as main_course JOIN (SELECT main_tran.courseID, COUNT(main_tran.takerID) as taker_amount FROM mainmodels_transaction as main_tran GROUP BY main_tran.courseID ORDER BY taker_amount DESC) as main_count ON main_course.courseID = main_count.courseID AND main_course.category_id = '+categoryID+' LIMIT 10;')
    bestRateCourses = Course.objects.raw('SELECT * FROM mainmodels_course as main_course JOIN (SELECT main_review.course_id, AVG(main_review.rating) as "average_rating" FROM mainmodels_review as main_review) as avg_main_review ON main_course.courseID = avg_main_review.course_id AND main_course.category_id = '+categoryID+' ORDER BY avg_main_review.average_rating DESC LIMIT 10;')
    featureCourses = FeaturedCourse.objects.raw('SELECT * FROM mainmodels_featuredcourse as main_feat JOIN mainmodels_course as main_course ON main_feat.course_id = main_course.courseID AND main_course.category_id = '+categoryID+' LIMIT 10;')
    # return renderBrowse(req, courseList, browseFilter)
    return render(req, 'browse/index.html', {'pageTitle' : category.categoryName, 'categories': categories, 'category' : category, 'mostPopularCourses': mostPopularCourses, 'bestRateCourses': bestRateCourses, 'featureCourses':featureCourses})
    # except:
        # return redirect(reverse('browse:browseIndex'))

def browseCategoryAll(req, categoryID):
    # try:
    categories = Category.objects.all()
    category = Category.objects.get(categoryID=categoryID)
    courses = Course.objects.filter(isDelete=False, isPublish=True, category=category).order_by('-createdDate')
    browseFilter = category.categoryName
    pageTitle = 'Browse ' + browseFilter
    # return renderBrowse(req, courseList, browseFilter)
    # except:
        # return redirect(reverse('browse:browseIndex'))
    return render(req, 'browse/all.html', {'pageTitle' : pageTitle, 'browseFilter' : browseFilter, 'categories' : categories, 'courses' : courses})