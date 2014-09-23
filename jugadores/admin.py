from django.contrib import admin

# Register your models here.
from .models import Jugador

class JugadorAdmin(admin.ModelAdmin):
    class Meta:
        model = Jugador

admin.site.register(Jugador, JugadorAdmin)