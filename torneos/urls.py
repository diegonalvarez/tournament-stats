from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin


urlpatterns = patterns("",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^cuenta/", include("account.urls")),
    #Include de las aplicaciones de las urls
    url(r'^', include('arbitros.urls', namespace="arbitros")),
    url(r'^', include('campeonatos.urls', namespace="campeonatos")),
    url(r'^', include('complejos.urls', namespace="complejos")),
    url(r'^', include('equipos.urls', namespace="equipos")),
    url(r'^', include('jugadores.urls', namespace="jugadores")),
    url(r'^', include('usuario.urls', namespace="usuarios")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
