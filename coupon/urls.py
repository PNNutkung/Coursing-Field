from django.conf.urls import url
from . import views

app_name = 'coupon'

urlpatterns = [
    url(r'^$', views.index, name='index')
    url(r'^add_coupon/$' , views.add_coupon , name='add_coupon'),
]
