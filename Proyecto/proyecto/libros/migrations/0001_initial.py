# Generated by Django 4.2.2 on 2023-06-15 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='sin nombrar', max_length=300, verbose_name='Titulo del libro')),
                ('edicion', models.CharField(default=0, max_length=300, verbose_name='Edicion del libro')),
                ('editorial', models.CharField(default=0, max_length=300, verbose_name='Editorial del libro')),
                ('año_pub', models.IntegerField(default=1992, verbose_name='Año de publicacion')),
                ('pagina', models.IntegerField(default=100, verbose_name='Numero de paginas')),
            ],
        ),
    ]
