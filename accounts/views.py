from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    numbers = [1,2,3,4,5,6]
    name = 'Adegoke Tosin'

    args = {
        'myName': name,
        'numbers': numbers,
    }
    return render(request, 'accounts/home.html', args)
    