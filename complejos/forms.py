from django import forms

from .models import Complejo

class ComplejoForm(forms.ModelForm):
    class Meta:
        model = Complejo


class ComplejoPublicForm(forms.ModelForm):
    class Meta:
        model = Complejo
        exclude = ('user',)