from django.urls import path
from .views import GetAddress, CreateAddress

app_name='addresses'
urlpatterns = [
    path('<int:id>/', GetAddress, name='detail'),
    path('create/', CreateAddress.as_view(), name='create')
]
