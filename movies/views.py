from django.shortcuts import render
from django.http import HttpResponse
from django import views
from .models import Movie

# Hay dos formas de crear vistas
# 1.- Creando una clase -> Tenemos dos o más métodos HTTP en la misma ruta
# 2.- Creando una función -> Sólo tenemos un método HTTP en la ruta

def GetMovies(request):
    # Vamos a traer todos las películas
    movies = Movie.objects.all() # SELECT * FROM movies_movie #queryset
    template_name = 'movies/list.html'
    context = {
        'movies': movies
    }
    return render(request, template_name, context)


def GetMovie(request, id):
    movie = Movie.objects.get(pk=id)
    template_name = 'movies/detail.html'
    context = {
        'movie': movie
    }
    return render(request, template_name, context)
