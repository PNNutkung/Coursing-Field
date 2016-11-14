from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from mainmodels.models import Course, FeaturedCourse
# Create your views here.
def index(req):
    mostPopularCourses = Course.objects.raw('SELECT * FROM mainmodels_course as main_course JOIN (SELECT main_tran.courseID, COUNT(main_tran.takerID) as taker_amount FROM mainmodels_transaction as main_tran GROUP BY main_tran.courseID ORDER BY taker_amount DESC) as main_count ON main_course.courseID = main_count.courseID LIMIT 10;')
    featureCourses = FeaturedCourse.objects.raw('SELECT * FROM mainmodels_featuredcourse as main_feat JOIN mainmodels_course as main_course ON main_feat.course_id = main_course.courseID LIMIT 10;')
    return render(req, 'index/main.html', {'pageTitle': 'Coursing Field', 'mostPopularCourses': mostPopularCourses, 'featureCourses': featureCourses})
