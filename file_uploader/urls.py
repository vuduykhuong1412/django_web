from wsgiref.handlers import format_date_time


from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.fileUploaderView),
]