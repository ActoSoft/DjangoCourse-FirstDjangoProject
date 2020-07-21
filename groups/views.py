from django.shortcuts import render, redirect
from django import views
from django.contrib import messages
from .models import GroupModel
from .forms import GroupModelForm

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

class CreateGroup(views.View):
    def get(self, request):
        form = GroupModelForm()
        template_name = 'groups/form.html'
        context = {
            'form': form
        }
        return render(request, template_name, context)

    def post(self, request):
        form = GroupModelForm(request.POST)
        if form.is_valid():
            new_group = form.save()
            messages.success(request, 'Grupo creado con éxito')
            return redirect('groups:detail', new_group.id)
        else:
            template_name = 'groups/form.html'
            context = {
                'form': form
            }
            messages.error(request ,'Algo falló al crear un grupo')
            return render(request, template_name, context)
