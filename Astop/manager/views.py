from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from .forms import ClientForm
from django.contrib.auth import get_user_model
from .models import Client

User = get_user_model()


# Create your views here.
def backdoor(request):
    return render(request, 'backdoor.html')

@require_http_methods(['GET', 'POST'])
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