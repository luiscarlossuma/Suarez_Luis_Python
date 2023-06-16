from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect

from .models import Libros
from .forms import LibroForm

def index(request):

    return HttpResponse("Hola mundo")

class Inicio(View):
    template_name = 'inicio.html'

    def post(self, request):
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')

        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = LibroForm()
        libros = Libros.objects.all()
        return render(request, self.template_name, {'form': form, 'libros': libros})

def insertar_libro(request):
    nuevo_libro = Libros(
        titulo='El gran libro',
        edicion='Primera edicion',
        editorial='Editorial XYZ',
        año_pub=2022,
        paginas=200
    )
    nuevo_libro.save()

    return HttpResponse('Libro insertado correctamente')