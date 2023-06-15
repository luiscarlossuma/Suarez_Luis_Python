from django.db import models

# Create your models here.
class Libros(models.Model):

    titulo = models.CharField('Titulo del libro', max_length=300, default='sin nombrar')
    edicion = models.CharField('Edicion del libro', max_length=300, default=0)
    editorial = models.CharField('Editorial del libro', max_length=300, default=0)
    año_pub = models.IntegerField('Año de publicacion', default=1992)
    paginas = models.IntegerField('Numero de paginas', default=100)

    def _str_(self):
        return self.titulo