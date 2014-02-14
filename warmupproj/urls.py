from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'warmupproj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/login$', 'warmupproj.users.views.handleLogin'),
    url(r'^users/add$', 'warmupproj.users.views.handleLogin'),

)
