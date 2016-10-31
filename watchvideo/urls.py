from django.conf.urls import url
from . import views

app_name = 'watchvideo'
urlpatterns = [
    url(r'^(?P<courseID>[0-9]+)/content/$', views.show_content_in_tabs, name='show_contents_in_tabs'),
]
