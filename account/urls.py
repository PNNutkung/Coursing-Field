from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profileUpdate/', views.profileUpdate, name='profileUpdate'),
    url(r'^personalUpdate/', views.personalUpdate, name='personalUpdate'),
    url(r'^updateProfilePicture/', views.updateProfilePicture, name='updateProfilePicture'),
]
