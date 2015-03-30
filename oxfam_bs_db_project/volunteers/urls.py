from django.conf.urls import url, patterns
from volunteers import views

__author__ = 'joshuamarsh'


urlpatterns = patterns('',

    url(r'^', views.index, name='index'),

    )