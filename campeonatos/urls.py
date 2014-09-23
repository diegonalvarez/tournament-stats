from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = patterns("",
    url(r'^campeonato/agregar$','campeonatos.views.agregar', name='agregar_torneo'),
    url(r'^campeonato/editar/$','campeonatos.views.editar', name='editar_torneo'),
    url(r'^campeonato/editar/(?P<id>\d+)/$','campeonatos.views.editar', name='editar_torneo'),
    url(r'^campeonato/encurso/$','campeonatos.views.encurso', name='encurso_torneo'),
    url(r'^campeonato/finalizados/$','campeonatos.views.finalizados', name='finalizados_torneo'),
    url(r'^campeonato/ver/(?P<id>\d+)/$','campeonatos.views.ver', name='ver_torneo'),
)