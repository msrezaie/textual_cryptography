from django.forms import ModelForm, Textarea
from . models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'title', 'message']
        widgets = {
            'message': Textarea(attrs={'cols': 30, 'rows': 10}),
        }