from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from mainmodels.models import Course, FeaturedCourse
# Create your views here.
def index(req):
    mostPopularCourses = Course.objects.raw('SELECT * FROM mainmodels_course as main_course JOIN (SELECT main_review.course_id, AVG(main_review.rating) as "average_rating" FROM mainmodels_review as main_review) as avg_main_review ON main_course.courseID = avg_main_review.course_id ORDER BY avg_main_review.average_rating LIMIT 10;')
    featureCourses = FeaturedCourse.objects.raw('SELECT * FROM mainmodels_featuredcourse as main_feat JOIN mainmodels_course as main_course ON main_feat.course_id = main_course.courseID LIMIT 10;')
    return render(req, 'index/main.html', {'pageTitle': 'Coursing Field', 'mostPopularCourses': mostPopularCourses, 'featureCourses': featureCourses})
