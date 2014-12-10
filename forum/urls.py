from django.conf.urls import patterns, url

from forum import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<topico_id>\d+)/$', views.visualizar_topico, name='topico'),
    url(r'^(?P<topico_id>\d+)/comentar/$', views.comentar, name='comentar'),
)