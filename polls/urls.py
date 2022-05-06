from django.urls import re_path

from.import views
app_name= "polls"

urlpatterns=[
    re_path(r'^$', views.index,name='index'),
    #regular expression for polls/5/
    re_path(r'^(?P<question_id>[0-9]+)/$', views.detail, name= 'detail'),
    #regular expression for polls/5/regular
    re_path(r'^(?P<question_id>[0-9]+)/results/$', views.results, name= 'results'),
    #regular expression for polls/5/vote
    re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    re_path(r'^detail/(?P<question_id>[0-9]+)/$', views.detail, name='details'),

    # re_path(r'^$', views.IndexView.as_view(), name='index'),
    # re_path(r'^(?P<pk>[[0-9]+)/$', views.IndexView.as_view(), name='detail'),
    # re_path(r'^(?P<pk>[[0-9]+)/results/$', views.IndexView.as_view(), name='result'),
    # re_path(r'^(?P<question_id>[0-9]]+)/vote/$', views.IndexView.as_view(), name='vote'),
]
    