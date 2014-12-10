from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangolive.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^forum/', include('forum.urls', namespace='forum')),
	#url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
)
