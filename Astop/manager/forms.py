from enum import unique

from django import forms
from django.contrib.auth import get_user_model

from manager.models import Client

User = get_user_model()

class ClientForm(forms.Form):

    first_name = forms.CharField(label='First Name', max_length=100,min_length=1,
                                 error_messages={'required':'Please enter first name'})
    last_name = forms.CharField(label='Last Name', max_length=100, min_length=1,
                                 error_messages={'required':'Please enter last name'})
    email = forms.CharField(label='Email', error_messages={'required':'Please enter email'})
    phone = forms.CharField(label='Phone', error_messages={'required':'Please enter phone'})
    address = forms.CharField(label='Address', max_length=100)
    city = forms.CharField(label='City', max_length=100)
    occupation = forms.CharField(label='Occupation', max_length=100)
    registration_code = forms.CharField(label='Registration Code', max_length=100)
    trade_name = forms.CharField(label='Trade Name', max_length=100)
    nzbn = forms.CharField(label='NZBN', max_length=100)

#ensure no same email address
    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = Client.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('Email already exists')
        return email


