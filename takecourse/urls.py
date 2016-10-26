from django.conf.urls import url
from . import views

app_name = 'takecourse'
urlpatterns = [
    url(r'^(?P<courseID>[0-9]+)/$', views.take_course, name='take_course'),
    # url(r'^confirmed/(?P<courseID>[0-9])/$'), views.confirmed_course, name='confirmed_course'),
]
