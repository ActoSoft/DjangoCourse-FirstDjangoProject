from django.urls import path
from .views import GetUsers, GetUser

app_name='users'
urlpatterns = [
    path('', GetUsers, name='list'),
    path('<int:id>', GetUser, name='detail')
]