"""coursing_field URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('index.urls')),
    url(r'^', include('account.urls')),
    url(r'^ui/', include('ui.urls')),
    url(r'^browse/', include('browse.urls')),
    url(r'^course/', include('course.urls')),
    url(r'^watchvideo/',include('watchvideo.urls')),
    url(r'^mockaccount/', include('mockaccount.urls')),
    url(r'^takecourse/', include('takecourse.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^admin/', admin.site.urls),
]
