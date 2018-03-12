from django.forms import ModelForm
from django import forms
from .models import Url

class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['url',]
        widgets = {
            'url': forms.TextInput(attrs={
                'placeholder' : 'type long url here',
                'class' : 'form-control form-control-lg'
            })
        }
