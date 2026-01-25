from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from .forms import ClientForm, LoginForm
from django.contrib.auth import get_user_model
from .models import Client
from functools import wraps

User = get_user_model()


# Create your views here.
@require_http_methods(['GET', 'POST'])
def backdoor(request):
    if request.method == 'GET':
        return render(request, 'backdoor.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            if username == "admin1" and password == "password":
                request.session['is_logged_in'] = True
                return redirect('manager:management')
            else:
                return render(request, 'backdoor.html', {'error': 'Invalid username or password'})
        else:
            return render(request,'backdoor.html', {'form': form})


def session_login_required(view_function):
    @wraps(view_function)
    def wrapped_view(request, *args, **kwargs):
        if not request.session.get('is_logged_in'):
            return redirect('manager:backdoor')
        return view_function(request, *args, **kwargs)
    return wrapped_view

@session_login_required
def management(request):
    if request.method == 'GET':
        return render(request, 'management.html')

    else:
        form = ClientForm(request.POST)
        if form.is_valid():

            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            city = form.cleaned_data.get('city')
            occupation = form.cleaned_data.get('occupation')
            registration_code = form.cleaned_data.get('registration_code')
            trade_name = form.cleaned_data.get('trade_name')
            nzbn = form.cleaned_data.get('nzbn')

            Client.objects.create(first_name = first_name, last_name=last_name, email=email, phone=phone,
                                      address=address, city=city, occupation=occupation,
                                      registration_code=registration_code, trade_name=trade_name,
                                      nzbn=nzbn)

            return render(request, 'management.html')
        else:
            print(form.errors)
            return render(request, 'management.html',context={'form':form})