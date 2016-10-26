from django.conf.urls import url
from . import views

app_name = 'course'
urlpatterns = [
    url(r'^create/$', views.createCourse, name='createCourse'),
    url(r'^(?P<courseID>[0-9]+)/$', views.view_course, name='view_course'),
]
