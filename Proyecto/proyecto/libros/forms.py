from django import forms
from .models import Libros

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['titulo', 'edicion', 'editorial', 'año_pub', 'paginas']

    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get('titulo')
        edicion = cleaned_data.get('edicion')
        editorial = cleaned_data.get('editorial')
        año_pub = cleaned_data.get('año_pub')
        paginas = cleaned_data.get('paginas')

        if not titulo or not edicion or not editorial or not año_pub or not paginas:
            raise forms.ValidationError("Todos los campos deben estar completos")
        return cleaned_data