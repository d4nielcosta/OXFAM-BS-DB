from django.conf.urls import patterns, include, url
from django.contrib import admin
from volunteers import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oxfam_bs_db_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('volunteers.urls')),#just added this
)
