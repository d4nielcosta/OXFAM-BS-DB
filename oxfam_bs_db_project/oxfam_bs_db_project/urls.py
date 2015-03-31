from django.conf.urls import patterns, include, url
from django.contrib import admin
from volunteers import views


urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^volunteers/', include('volunteers.urls')),

)
