from django.shortcuts import render
from .models import GroupModel

def GetGroups(request):
    groups = GroupModel.objects.all()
    template_name = 'groups/list.html'
    context = {
        'groups': groups
    }
    return render(request, template_name, context)

def GetGroup(request, id):
    group = GroupModel.objects.get(id=id)
    template_name = 'groups/detail.html'
    context = {
        'group': group
    }
    return render(request, template_name, context)