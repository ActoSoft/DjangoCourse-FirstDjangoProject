from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import views
from .models import Movie
from .forms import MovieForm

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

class CreateMovie(views.View):
    def get(self, request):
        template_name = 'movies/form.html'
        return render(request, template_name)

    def post(self, request):
        data = request.POST
        new_movie = Movie.objects.create(
            title=data['title'],
            sinopsis=data['sinopsis'],
            duration=data['duration'],
            calif=data['calif'],
            gender=data['gender']
        )
        if new_movie:
            print('Película creada con éxito!')
            return redirect('/movies/')
        else:
            print('La película no se pudo crear')
            return redirect('/movies/create/')

class CreateMovieEasy(views.View):
    def get(self, request):
        form = MovieForm()
        template_name = 'movies/form_easy.html'
        context = {
            'form': form
        }
        return render(request, template_name, context)

    def post(self, request):
        new_form = MovieForm(request.POST)
        if new_form.is_valid():
            new_movie = new_form.save()
            print('Se creó la película corerctamente', new_movie)
            return redirect('/movies/')
        else:
            template_name = 'movies/form_easy.html'
            context = {
                'form': new_form
            }
            return render(request, template_name, context)
