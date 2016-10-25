from django.conf.urls import url
from . import views

app_name = 'course'
urlpatterns = [
    url(r'^create/$', views.createCourse, name='createCourse'),
]
