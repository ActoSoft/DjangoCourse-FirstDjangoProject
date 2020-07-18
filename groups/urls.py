from django.urls import path
from .views import GetGroups, GetGroup, CreateGroup

app_name='groups'
urlpatterns = [
    path('', GetGroups, name='list'),
    path('<int:id>', GetGroup, name='detail'),
    path('create/', CreateGroup.as_view(), name='create')
]