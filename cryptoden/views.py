from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Operation, Page
from . forms import CryptodenRegisterForm
from base.models import Profile
import json
import importlib

def userSignin(request):
    form_type = 'signin'
    page = Page.objects.first()
    profile = Profile.objects.first()

    if request.user.is_authenticated:
        return redirect('cryptoden:crypto-main')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist!")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('cryptoden:crypto-main')
        else:
            messages.error(request, "Username/Password incorrect!")

    context = {
        'profile': profile,
        'pages': page,
        'form_type': form_type
    }
    return render(request, "cryptoden/signin_register.html", context)

def userRegister(request):
    form_type = 'register'
    page = Page.objects.first()
    profile = Profile.objects.first()
    form = CryptodenRegisterForm()

    if request.method == 'POST':
        form = CryptodenRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cryptoden:crypto-main')
        
    context = {
        'profile': profile,
        'pages': page,
        'form_type': form_type,
        'form': form
    }
    return render(request, "cryptoden/signin_register.html", context)

def userAccount(request):
    page = Page.objects.first()
    profile = Profile.objects.first()

    if not request.user.is_authenticated:
        return redirect('cryptoden:crypto-main')

    context = {
        'profile': profile,
        'pages': page,
    }
    return render(request, "cryptoden/account.html", context)


def userLogout(request):
    logout(request)
    return redirect('cryptoden:crypto-main')

@csrf_exempt  # disable CSRF protection
def index(request):
    if request.method == 'POST':  # check if request method is POST
        # Get JSON data from request body and decode it
        recieved_data = json.loads(request.body.decode("utf-8"))

        # Extract keys, cipher, method, and text values from the received JSON data
        keys, cipher, method, text = recieved_data['keys'], recieved_data['cipher'], recieved_data['method'], recieved_data['text']

        try:
            # Import the module for the specified cipher
            module = importlib.import_module(f'cryptoden.ciphers.{cipher}')

            # Get the function for the specified encryption/decryption method
            cipher_function = getattr(module, method)

            # Call the specified cipher function with the provided text and keys
            result = cipher_function(text, keys)
            
            # Return the encrypted/decrypted text as an HTTP response
            return HttpResponse(result)

        except ImportError:
            # If the specified cipher module could not be found, print an error message
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