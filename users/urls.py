from django.urls import path
from .views import GetUsers, GetUser, CreateUser

app_name='users'
urlpatterns = [
    path('', GetUsers, name='list'),
    path('<int:id>/', GetUser, name='detail'),
    path('create/', CreateUser.as_view(), name='create')
]