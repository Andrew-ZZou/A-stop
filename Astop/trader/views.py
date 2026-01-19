from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import TraderForm, LoginForm
from django.contrib.auth import login, authenticate
from .models import Trader
from django.contrib.auth.hashers import make_password
from manager.models import Client
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

# register trader promo details
@require_http_methods(['GET', 'POST'])
def registration(request):
    if request.method == 'GET':
        form = TraderForm()
        return render(request, 'registration.html', {'form': form})
    else:
        form = TraderForm(request.POST)
        if form.is_valid():

            client_id_value = form.cleaned_data.get('client_id')
            password = make_password(form .cleaned_data.get('password'))
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')

            try:
                client = Client.objects.get(client_id=client_id_value)
            except Client.DoesNotExist:
                form.add_error('client_id', 'Client ID not found')
                return render(request, 'registration.html',{'form': form})

            Trader.objects.create(client_id=client, password=password, email=email, phone_number=phone_number)
            return redirect('trader:login')

        else:
            return render(request, 'registration.html', {'form': form})
#trader login
@require_http_methods(['GET', 'POST'])
def alogin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'login.html')
        else:

            return render(request, 'login.html')


def test(request):
    return render(request, 'test.html')


