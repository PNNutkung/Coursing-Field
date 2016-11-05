from django.conf.urls import url
from . import views

app_name = 'ui'

urlpatterns = [

    url(r'^$' , views.index , name='index'),
    url(r'^view$' , views.view , name='view'),
    url(r'^browse$' , views.browse , name='browse'),
    url(r'^register$' , views.register , name='register'),
    url(r'^create$' , views.create , name='create'),
    url(r'^profile$' , views.profile , name='profile'),
    url(r'^tester$' , views.tester , name='tester'),



]
