from django.shortcuts import render, redirect
from django import views
from .models import Address
from .forms import AddressForm

def GetAddress(request, id):
    address = Address.objects.get(pk=id)
    template_name = 'addresses/detail.html'
    context = {
        'address': address
    }
    return render(request, template_name, context)

class CreateAddress(views.View):
    def get(self, request):
        form = AddressForm()
        template_name = 'addresses/form.html'
        context = {
            'form':form
        }
        return render(request, template_name, context)

    def post(self, request):
        new_form = AddressForm(request.POST) #Recibe la info desde la web
        if new_form.is_valid():
            new_address = new_form.save()
            return redirect('users:list')
        else:
            template_name = 'addresses/form.html'
            context = {
                'form': new_form
            }
            return render(request, template_name, context)

class UpdateAddress(views.View):
    def get(self, request, id):
        address = Address.objects.get(pk=id)
        form = AddressForm(instance=address)
        template_name = 'addresses/form.html'
        context = {
            'form': form,
            'address': address
        }
        return render(request, template_name, context)
    def post(self, request, id):
        address = Address.objects.get(pk=id)
        form_updated = AddressForm(request.POST, instance=address)
        if form_updated.is_valid():
            form_updated.save()
            return redirect('addresses:detail', address.id)
        else:
            template_name = 'addresses/form.html'
            context = {
                'form': form_updated,
                'address': address
            }
            return render(request, template_name, context)

def DeleteAddress(request, id):
    address = Address.objects.get(pk=id)
    user = address.user
    address.delete()
    return redirect('users:detail', address.user.id)