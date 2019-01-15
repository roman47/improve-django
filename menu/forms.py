from django import forms

from .models import Menu, Item

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        exclude = ('created_date',)