from django.urls import path
from .views import GetUsers

app_name='users'
urlpatterns = [
    path('', GetUsers, name='list')
]