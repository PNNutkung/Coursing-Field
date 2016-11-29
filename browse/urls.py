from django.conf.urls import url
from . import views

app_name = 'browse'
urlpatterns = [
    url(r'^$', views.browseIndex, name='browseIndex'),
    url(r'^all/$', views.browseAll, name='all'),
    url(r'^(?P<categoryID>[0-9]+)/$', views.browseCategory, name='browseCategory'),
    url(r'^(?P<categoryID>[0-9]+)/all/$', views.browseCategoryAll, name='browseCategoryAll')
]
