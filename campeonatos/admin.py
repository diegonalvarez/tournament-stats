from django.contrib import admin

# Register your models here.
from .models import Campeonato

class CampeonatoAdmin(admin.ModelAdmin):
    class Meta:
        model = Campeonato

admin.site.register(Campeonato, CampeonatoAdmin)

