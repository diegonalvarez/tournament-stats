from django import forms

from .models import Campeonato
from equipos.models import Equipo
from django.contrib.auth.models import User

class CampeonatoForm(forms.ModelForm):
    equipos = forms.ModelMultipleChoiceField(queryset = Equipo.objects.all().filter(complejo_id__user = 1), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Campeonato

class CampeonatoPublicForm(forms.ModelForm):
    equipos = forms.ModelMultipleChoiceField(queryset = Equipo.objects.all(), widget=forms.CheckboxSelectMultiple)
