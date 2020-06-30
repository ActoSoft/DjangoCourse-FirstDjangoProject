from django.urls import path
from .views import GetMovies, GetMovie, CreateMovie, CreateMovieEasy

urlpatterns = [
    path('', GetMovies),
    path('<int:id>/', GetMovie),
    path('create/', CreateMovieEasy.as_view())
]