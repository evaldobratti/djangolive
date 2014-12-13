from django.conf.urls import patterns, url

from forum import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^topico/(?P<topico_id>\d+)/$', views.visualizar_topico, name='topico'),
    url(r'^topico/(?P<topico_id>\d+)/comentar/$', views.comentar, name='comentar'),
    url(r'^categoria/(?P<categoria_id>\d+)/$', views.visualizar_categoria, name='categoria'),
    url(r'^categoria/(?P<categoria_id>\d+)/novo_topico/$', views.novo_topico, name='novo_topico'),
    url(r'^categoria/(?P<categoria_id>\d+)/novo_topico_criar/$', views.novo_topico_criar, name='novo_topico_criar'),
)