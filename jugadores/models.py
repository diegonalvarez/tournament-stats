from django.db import models
from django.utils.encoding import smart_unicode
from equipos.models import Equipo

# Create your models here.
class Jugador(models.Model):
    nombre = models.CharField(max_length=120, null=False, )
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    equipo_id = models.ForeignKey(Equipo)

    def __unicode__(self):
        return smart_unicode(self.nombre)