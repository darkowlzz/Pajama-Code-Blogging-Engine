from django.conf.urls.defaults import patterns, include, url
from pblog.views import home

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^home/$', home),
    url(r'^post/', include('pblog.post.urls')),
    # Examples:
    # url(r'^$', 'pblog.views.home', name='home'),
    # url(r'^pblog/', include('pblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
