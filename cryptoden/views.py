from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . models import Operation, Page
from base.models import Profile

from cryptoden.ciphers import caesar

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        plainText = request.POST.get('plainText')
        caesarKey = request.POST.get('caesarKey')
        # process the plaintext and key with the caesar cipher
        cipherText = caesar.encrypt(plainText, int(caesarKey))
        # return the ciphertext as a response
        return HttpResponse(cipherText)

    operation = Operation.objects.all()
    page = Page.objects.first()
    profile = Profile.objects.first()

    context = {
        'profile': profile,
        'operations': operation,
        'pages': page
    }

    return render(request, "cryptoden/index.html", context)