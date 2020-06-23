from django.urls import path
from .views import GetMovies, GetMovie

urlpatterns = [
    path('', GetMovies),
    path('<int:id>/', GetMovie)
]