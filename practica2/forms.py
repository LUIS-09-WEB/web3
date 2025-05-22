from django import forms
from .models import practica

class practicaForm(forms.ModelForm):
    class Meta:
        model = practica
        fields = ['nombre', 'correo', 'comentarios']