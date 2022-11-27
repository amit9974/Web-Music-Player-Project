from django import forms
from django.contrib.auth.models import User




#Register Form
class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Create Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("Username is already exists")
        return username



    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact='email')
        if qs.exists():
            raise forms.ValidationError('Email address is already used')
        return email


#Login Form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')


    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError('Invalid username please check!')
        return username

    