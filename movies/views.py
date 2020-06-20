from django.shortcuts import render
from django.http import HttpResponse
from django import views
from .models import Movie

# Hay dos formas de crear vistas
# 1.- Creando una clase -> Tenemos dos o más métodos HTTP en la misma ruta
# 2.- Creando una función -> Sólo tenemos un método HTTP en la ruta

def GetMovies(request):
    # Vamos a traer todos las películas
    #"SELECT * FROM movies_movie WHERE jsdlkdfjsdklsfjsklfsjkld" -> Aquí no hacemos esto.
    movies = Movie.objects.all() #SELECT * FROM movies_movie #queryset
    print(movies)
    return HttpResponse('Funciona!')
