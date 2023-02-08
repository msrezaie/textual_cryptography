from django.shortcuts import render
from . models import Operation

# Create your views here.

def index(request):
    operation = Operation.objects.all()
    return render(request, "cryptoden/index.html", {'operations': operation})
