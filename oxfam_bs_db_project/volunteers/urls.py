from django.conf.urls import url, patterns

import views


urlpatterns = patterns('',


                       url(r'^$', views.index, name='index'),

                       #Profile Related
                       url(r'^profile/(?P<volunteer_id>[\w\-]+)/$', views.profile, name='profile'),


                       )
