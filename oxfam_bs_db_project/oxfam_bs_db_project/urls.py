from django.conf.urls import patterns, include, url
from django.contrib import admin
from volunteers import views


urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^volunteers/', include('volunteers.urls')),

)

handler400 = 'volunteers.views.handle404'
handler404 = 'volunteers.views.handle404'
handler500 = 'volunteers.views.handle404'

