from django.urls import path
from .views import GetGroups, GetGroup

app_name='groups'
urlpatterns = [
    path('', GetGroups, name='list'),
    path('<int:id>', GetGroup, name='detail')
]