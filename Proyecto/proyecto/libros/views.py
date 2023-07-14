from django.http import HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect

from .models import Libros
from .forms import LibroForm

def index(request):

    return HttpResponse("Hola mundo")

class Inicio(View):
    template_name = 'inicio.html'

    def post(self, request):

        return render(request, self.template_name)

    def get(self, request):
        libros = Libros.objects.all()
        return render(request, self.template_name, {'libros': libros})

class Formulario(View):
    template_name = 'formulario.html'

    def post(self, request):
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = LibroForm()
        return render(request, self.template_name, {'form': form})

class EliminarLibro(View):
    def post(self, request, libro_id):
        libro =get_object_or_404(Libros, pk=libro_id)
        libro.delete()
        return redirect('inicio')

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