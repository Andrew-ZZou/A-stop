from django import forms
from django.contrib.auth import get_user_model

from Astop.manager.models import Client

User = get_user_model()

class ClientForm(forms.Form):
    client_id = forms.CharField(label='Client ID', max_length=100)
    email = forms.EmailField(label='Email', error_messages={'required':'Please enter email'})
    phone_number = forms.CharField(label='Phone Number', error_messages={'required':'Please enter phone number'})
    password = forms.CharField(widget=forms.PasswordInput,label= 'Password', error_messages={'required':'Please enter password'})
    promo_title = forms.CharField(label='Promo Title', error_messages={'required':'Please enter promo title'})
    promo_content1 = forms.CharField(widget=forms.Textarea, label='Promo Content', error_messages={'required':'Please enter promo content'})
    promo_content2 = forms.CharField(widget=forms.Textarea, label='Promo Content', error_messages={'required':'Please enter promo content'})
    promo_content3 = forms.CharField(widget=forms.Textarea, label='Promo Content', error_messages={'required':'Please enter promo content'})

#ensure no same email address
    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('Email already exists')
        return email

    def clean_client_id(self):
        client_id = self.cleaned_data.get('client_id')
        exists = Client.objects.filter(client_id=client_id).exists()
        if exists:
            raise forms.ValidationError('Client ID already exists')
        return client_id