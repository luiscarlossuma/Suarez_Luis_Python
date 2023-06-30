from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

def index(request):

    return HttpResponse("Aqui se deberian mostar los productos")

class Inicio(View):
    template_name = 'inicio.html'

    def post():

        return

    def get(self, request):

        print('yainicio mi GET-----*')

        return render(request, self.template_name)
