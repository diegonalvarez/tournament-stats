from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = patterns("",
    url(r'^equipo/agregar$','equipos.views.agregar', name='agregar_equipo'),
    url(r'^equipo/editar/$','equipos.views.editar', name='editar_equipo'),
    url(r'^equipo/editar/(?P<id>\d+)/$','equipos.views.editar', name='editar_equipo'),
    url(r'^equipo/lista$','equipos.views.lista', name='lista_equipo'),
)