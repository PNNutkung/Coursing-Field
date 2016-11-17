from django.shortcuts import render_to_response
from mainmodels.models import Course
# Create your views here.
def search_titles(req):
    str_query = '%%%s%%'%(req.POST.get('search_text', ''))
    print (str_query)
    courses = Course.objects.raw("SELECT course.courseID, course.courseName, user.username FROM mainmodels_course as course JOIN auth_user as user ON user.id = course.owner_id WHERE course.isPublish = 1 AND course.isDelete = 0 AND course.courseName LIKE %s;",[str_query])
    return render_to_response('search/search.html', {'courses': courses})
