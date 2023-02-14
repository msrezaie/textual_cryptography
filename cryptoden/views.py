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
        keys = recieved_data['keys']
        for cipher_name, key_value in keys.items():
        # Extract the cipher name from the key name
            try:
                # Import the cipher module
                module = importlib.import_module(f'cryptoden.ciphers.{cipher_name}')
                # Get the plaintext value
                plaintext = recieved_data['text']
                # Call the encrypt() or decrypt() method based on the operation
                # result = module.encrypt(plaintext, int(key_value))
                cipher_function = getattr(module, "encrypt")
                # Use the result
                # print()
                result = cipher_function(plaintext, int(key_value))
                return HttpResponse(result)

            except ImportError:
                print(f"Error: the cipher '{cipher_name}' was not found.")

    operation = Operation.objects.all()
    page = Page.objects.first()
    profile = Profile.objects.first()

    context = {
        'profile': profile,
        'operations': operation,
        'pages': page
    }

    return render(request, "cryptoden/index.html", context)