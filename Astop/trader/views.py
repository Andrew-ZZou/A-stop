from django.shortcuts import render

# Create views.

def index(request):
    return render(request, 'index.html')


def plumbers(request):
    return render(request, 'plumbers.html')


def details(request, client_id):
    return render(request, 'details.html')


def registration(request):
    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html')


def test(request):
    return render(request, 'test.html')


