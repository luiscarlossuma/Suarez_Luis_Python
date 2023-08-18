from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    # Agregando un campo adicional para el correo electronico (EmailField)
    email = forms.EmailField()

    class Meta:
        # Especificando el modelo con el que esta relacionado el formulario (User en este caso)
        model = User
        # Especificando los campos que se mostraran en el formulario y su su orden
        fields = ['username', 'email', 'password1', 'password2']