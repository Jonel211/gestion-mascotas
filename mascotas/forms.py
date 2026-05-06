from django import forms
from .models import Mascota, Dueno

class DuenoForm(forms.ModelForm):
    class Meta:
        model = Dueno
        fields = '__all__'


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'