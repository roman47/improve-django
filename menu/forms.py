from django import forms
from django.core.exceptions import ValidationError

from .models import Menu, Item

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        exclude = ('created_date',)

    def clean(self):
        self_str = self.cleaned_data['season']
        #import pdb;
        #pdb.set_trace()
        if not (self_str.isalpha()):
            raise ValidationError(
                "Season must be only letters, no spaces allowed either")

