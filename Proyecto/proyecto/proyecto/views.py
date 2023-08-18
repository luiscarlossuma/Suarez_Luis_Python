from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout

from .forms import UserRegistrationForm

def custom_logout(request):
    logout(request)
    return redirect('/libros/inicio')

def custom_login(request):
    template_name = 'login.html'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            print('-----------> Si entró al login')
            return redirect('/libros/inicio')
        else:
            print('-----------> No entró al login')
            messages.error(request, 'Credenciales invalidas')


    return render(request, template_name)

# View para registro de usuarios
def register(request):
    #Verificar si la solicitud es del tipo POST (envio de datos del formulario)
    if request.method == 'POST':
        # Crear una instancia del formulario de registro (con los datos enviados en la solicitud)
        form = UserRegistrationForm(request.POST)
        # Verificar si el formulario es valido (todos los campos requeridos estan completos y las validaciones pasaron)
        if form.is_valid():
            # Guardar los datos del formulario en la base de datos (crear un nuevo usuario)
            form.save()
            # Obtener el nombre de usuario ingresado en el formulario
            username = form.cleaned_data.get('username')
            # Obtener la contraseña ingresada en el formulario (la contraseña ya esta hasheada)
            password = form.cleaned_data.get('password1')
            # Autenticar al nuevo usuario recien registrado
            user = authenticate(username=username, password=password)
            # Iniciar sesion del usuario en la sesion actual
            login (request, user)
            # Redireccionar al usuario a la pagina de inicio
            return redirect('inicio')
    else:
        # Si la solicitud no es del tipo POST, crear una instancia de formulario en blanco
        form = UserRegistrationForm()
    # Renderizar la plantilla de registro con el formulario (Ya sea en blanco o con los datos ingresados previamente)
    return render (request, 'registration/register.html', {'form': form})