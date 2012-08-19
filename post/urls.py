from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('pblog.post.views',
    url(r'submit/$', 'send_post'),
    url(r'list/$', 'list_post'),
    url(r'blog/(?P<title>\w+)/$', 'show_post'),
)
