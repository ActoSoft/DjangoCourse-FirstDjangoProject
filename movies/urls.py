from django.urls import path
from .views import GetMovies, GetMovie, CreateMovie, CreateMovieEasy, UpdateMovie, DeleteMovie

urlpatterns = [
    path('', GetMovies),
    path('<int:id>/', GetMovie),
    path('create/', CreateMovieEasy.as_view()),
    path('update/<int:id>/', UpdateMovie.as_view()),
    path('delete/<int:id>/', DeleteMovie)
]