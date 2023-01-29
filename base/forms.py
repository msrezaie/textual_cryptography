from django import forms
from django.forms import ModelForm, Textarea
from . models import Contact

class ContactForm(ModelForm):
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'title', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'cont-message', 'placeholder': 'Message'}),
            'name': forms.TextInput(attrs={'class': 'cont-name', 'placeholder': 'Name'}),
            'title': forms.TextInput(attrs={'class': 'cont-title', 'placeholder': 'Title'}),
            'email': forms.EmailInput(attrs={'class': 'cont-email', 'placeholder': 'Email Address'}),
        }