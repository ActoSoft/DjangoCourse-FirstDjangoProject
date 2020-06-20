from django.urls import path
from .views import GetMovies

urlpatterns = [
    path('', GetMovies)
]
