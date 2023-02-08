from django.shortcuts import render
from . models import Operation, Page

# Create your views here.

def index(request):
    operation = Operation.objects.all()
    page = Page.objects.first()
    return render(request, "cryptoden/index.html", {'operations': operation, 'pages': page})
