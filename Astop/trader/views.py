from django.shortcuts import render

# Create views.

def index(request):
    return render(request, 'index.html')


def plumber(request):
    return render(request, 'plumber.html')

def electrician(request):
    return render(request, 'electrician.html')

def handyman(request):
    return render(request, 'handyman.html')


def details(request, client_id):
    return render(request, 'details.html')


def registration(request):
    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html')


def test(request):
    return render(request, 'test.html')


