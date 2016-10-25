from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mainmodels.models import Course
# Create your views here.
def browseIndex(req):
    '''Return the last courses.'''
    courseList = Course.objects.filter(isDelete=False)
    paginator = Paginator(courseList, 4)
    page = req.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    return render(req ,'browse/index.html', {'pageTitle': 'Browse courses', 'browseFilter': 'All courses','courses': courses, 'pageRange': paginator.page_range})
