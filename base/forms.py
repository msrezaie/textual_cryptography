from django import forms
from django.forms import ModelForm
from . models import Contact

class ContactForm(ModelForm):
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'title', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'cont-message, form-control', 'placeholder': 'Message'}),
            'name': forms.TextInput(attrs={'class': 'cont-name, form-control', 'placeholder': 'Name'}),
            'title': forms.TextInput(attrs={'class': 'cont-title, form-control', 'placeholder': 'Title'}),
            'email': forms.EmailInput(attrs={'class': 'cont-email, form-control', 'placeholder': 'Email Address'}),
        }