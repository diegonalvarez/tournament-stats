from django.db import models
from django.utils.encoding import smart_unicode
from complejos.models import Complejo

# Create your models here.
class Arbitro(models.Model):
    nombre = models.CharField(max_length=120, null=False, )
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    complejo_id = models.ForeignKey(Complejo)

    def __unicode__(self):
        return smart_unicode(self.nombre)