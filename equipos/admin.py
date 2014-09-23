from django.contrib import admin

# Register your models here.
from .models import Equipo

class EquipoAdmin(admin.ModelAdmin):
	class Meta:
		model = Equipo

admin.site.register(Equipo, EquipoAdmin)