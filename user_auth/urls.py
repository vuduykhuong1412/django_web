from django.urls import re_path
from atexit import register

from. import views
urlpatterns = [
    re_path(r'^register$', views.register)
     
 ]
 