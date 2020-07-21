from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label='Nombre de usuario')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
        'email', 'is_active', 'is_staff', 'is_superuser',
        'password']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
        'email', 'is_active', 'is_staff', 'is_superuser']

class ProfileForm(forms.ModelForm):
    gender = forms.CharField(label='Género')
    phone = forms.CharField(label='Teléfono')
    class Meta:
        model = Profile
        exclude = ['user']