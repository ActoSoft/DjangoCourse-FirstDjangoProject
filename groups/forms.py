from django import forms
from .models import GroupModel

class GroupModelForm(forms.ModelForm):
    class Meta:
        model = GroupModel
        fields = '__all__'