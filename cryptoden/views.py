from django.shortcuts import render
from . models import Operation, Page
from base.models import Profile

# Create your views here.

def index(request):
    operation = Operation.objects.all()
    page = Page.objects.first()
    profile = Profile.objects.first()

    context = {
        'profile': profile,
        'operations': operation,
        'pages': page
    }

    return render(request, "cryptoden/index.html", context)
