"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path
from  django.urls import include, re_path

urlpatterns = [
    re_path(r'^polls/', include('polls.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^user-auth/', include('user_auth.urls')),
    re_path(r'^file-upload/', include('file_uploader.urls')),
    re_path(r'^pagination/', include('pagination.urls')),
    re_path(r'^login/', include('login.urls')),
]

