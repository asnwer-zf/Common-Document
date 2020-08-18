"""mywebsit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homepage),
    url(r'^year/(\d{4})$', views.pageyear),
    url(r'^birthday/(\d{4})/(\d{1,2})/(\d{1,2})$', views.birthday),
    url(r'^person/(?P<name>\w+)/(?P<age>\d+)', views.person),
    url(r'^(?P<first>\d+)/add/(?P<last>\d+)', views.add)
]
