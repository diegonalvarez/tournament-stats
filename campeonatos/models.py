from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
from complejos.models import Complejo
from equipos.models import Equipo

# Create your models here.
class Campeonato(models.Model):
    nombre = models.CharField(max_length=120, null=False, )
    fecha_inicio = models.DateField(blank=True)
    cantidad_equipos = models.IntegerField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    complejo_id = models.ForeignKey(Complejo)
    estado_torneo = models.BooleanField(default=1)
    equipos = models.ManyToManyField(Equipo, blank=True)

    def is_active(self):
        return bool(self.active_status)

    def __unicode__(self):
        return smart_unicode(self.nombre)