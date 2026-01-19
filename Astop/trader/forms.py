from django import forms
from .models import Trader
from manager.models import Client
from django.contrib.auth.hashers import make_password


class TraderForm(forms.Form):
    client_id = forms.CharField(label='Client ID', max_length=100)
    registration_code = forms.CharField(label='Registration Code', max_length=100)
    email = forms.EmailField(label='Email', error_messages={'required':'Please enter email'})
    phone_number = forms.CharField(label='Phone Number', error_messages={'required':'Please enter phone number'})
    password = forms.CharField(widget=forms.PasswordInput,label= 'Password', error_messages={'required':'Please enter password'})
    confirm_password = forms.CharField(label='Confirm Password', error_messages={'required':'Please enter password'})
    about_myself = forms.CharField(required= False)
    promo_title = forms.CharField(required= False)
    promo_content1 = forms.CharField(widget=forms.Textarea, required= False)
    promo_content2 = forms.CharField(widget=forms.Textarea, required= False)
    promo_content3 = forms.CharField(widget=forms.Textarea, required= False)

#ensure no same email address
    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = Trader.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('Email already exists')
        return email

# ensure password match
    def clean(self):
        clean_data =super().clean()
        password = clean_data.get('password')
        confirm_password = clean_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')

# check client_id and registration code from Client table

        client_id = clean_data.get('client_id')
        registration_code = clean_data.get('registration_code')

        if client_id and registration_code:

            match = Client.objects.filter(client_id=client_id, registration_code=registration_code).exists()

            if not match:
                raise forms.ValidationError('Client ID and Registration Code do not match')
        return clean_data

    def clean_client_id(self):
        client_id = self.cleaned_data.get('client_id')
        exists = Trader.objects.filter(client_id=client_id).exists()
        if exists:
            raise forms.ValidationError('Client ID already exists')
        return client_id


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', error_messages={'required':'Please enter email'})
    password = forms.CharField(widget=forms.PasswordInput,label='Password', error_messages={'required':'Please enter password'})
