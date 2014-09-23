from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = patterns("",
    url(r'^torneo/agregar$','complejos.views.agregar', name='arb'),
    url(r'^torneo/editar/$','complejos.views.editar', name='arb'),
    url(r'^torneo/editar/(?P<id>\d+)/$','complejos.views.editar', name='arb'),
    
)