from django.shortcuts import render
from django.contrib.auth.models import User

def GetUsers(request):
    users = User.objects.filter(is_superuser=False)
    template_name = "users/list.html"
    context = {
        'users': users
    }
    return render(request, template_name, context)

def GetUser(request, id):
    user = User.objects.get(id=id)
    template_name = "users/detail.html"
    context = {
        'user': user
    }
    return render(request, template_name, context)



