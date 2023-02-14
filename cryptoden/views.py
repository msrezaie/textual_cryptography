from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . models import Operation, Page
from base.models import Profile
import json
import importlib

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        recieved_data = json.loads(request.body.decode("utf-8"))
        # Get values from JSON
        keys, cipher, method, text = recieved_data['keys'], recieved_data['cipher'], recieved_data['method'], recieved_data['text']

        try:
            # Import the cipher module
            module = importlib.import_module(f'cryptoden.ciphers.{cipher}')

            cipher_function = getattr(module, method)

            result = cipher_function(text, keys)
            
            return HttpResponse(result)

        except ImportError:
            print(f"Error: the cipher '{cipher}' was not found.")

    operation = Operation.objects.all()
    page = Page.objects.first()
    profile = Profile.objects.first()

    context = {
        'profile': profile,
        'operations': operation,
        'pages': page
    }

    return render(request, "cryptoden/index.html", context)