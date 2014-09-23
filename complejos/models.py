from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User

# Create your models here.
class Complejo(models.Model):
    nombre = models.CharField(max_length=120, null=False, )
    direccion = models.CharField(max_length=120, null=True, )
    telefono = models.CharField(max_length=120, null=True,)
    latitud = models.CharField(max_length=120, null=True, blank=True)
    longitud = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return smart_unicode(self.nombre)