from django.contrib import admin

# Register your models here.
from .models import Arbitro

class ArbitroAdmin(admin.ModelAdmin):
    class Meta:
        model = Arbitro

admin.site.register(Arbitro, ArbitroAdmin)