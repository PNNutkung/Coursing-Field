from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mainmodels.models import Course, Category
# Create your views here.
def browseIndex(req):
    category = Category.objects.all()
    return render(req, 'browse/index.html', {'pageTitle': 'Browse', 'categories': category})

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
