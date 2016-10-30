from django.conf.urls import url
from . import views

app_name = 'course'
urlpatterns = [
    url(r'^create/$', views.createCourse, name='createCourse'),
    url(r'^(?P<courseID>[0-9]+)/$', views.view_course, name='view_course'),
    url(r'^(?P<courseID>[0-9]+)/manage/$', views.manage_course, name='manage_course'),
    url(r'^(?P<courseID>[0-9]+)/edited_course/$', views.edited_course, name='edited_course'),
    url(r'^(?P<courseID>[0-9]+)/upload/$', views.upload_video, name='upload_video'),
    url(r'^(?P<courseID>[0-9]+)/(?P<videoID>[0-9]+)/comment/$', views.comment_on_video, name='comment_on_video'),
    url(r'^review/(?P<courseID>[0-9]+)/$', views.reviewCourse, name='reviewCourse'),
]
