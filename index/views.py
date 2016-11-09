from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from mainmodels.models import Course, Review
# Create your views here.
def index(req):
    mostPopularCourses = Course.objects.raw('SELECT * FROM mainmodels_course as main_course JOIN (SELECT main_review.course_id, AVG(main_review.rating) as "average_rating" FROM mainmodels_review as main_review) as avg_main_review ON main_course.courseID = avg_main_review.course_id ORDER BY avg_main_review.average_rating;')
    return render(req, 'index/main.html', {'pageTitle': 'Coursing Field', 'mostPopularCourses': mostPopularCourses})
