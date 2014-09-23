from django.contrib import admin

# Register your models here.
from .models import Complejo

class ComplejoAdmin(admin.ModelAdmin):
	class Meta:
		model = Complejo

admin.site.register(Complejo, ComplejoAdmin)