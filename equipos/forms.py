from django import forms

from .models import Equipo

class EquiposForm(forms.ModelForm):
    class Meta:
        model = Equipo