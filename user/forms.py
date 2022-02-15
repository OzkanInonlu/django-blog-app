from django import forms
from django.shortcuts import render, HttpResponse
                
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username')

    password = forms.CharField(max_length=20, widget=forms.PasswordInput(), label='Password')

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username')

    password = forms.CharField(max_length=20, widget=forms.PasswordInput(), label='Password')

    confirmPassword = forms.CharField(max_length=20, widget=forms.PasswordInput(), label='Confirm Password')

    def clean(self): #django'nun form methodu parola doğrulamak için

        username = self.cleaned_data['username']

        password = self.cleaned_data['password']

        confirmPassword = self.cleaned_data['confirmPassword']

        if (username and password and confirmPassword) and (password != confirmPassword):
            raise forms.ValidationError("Passwords are not mathced !!") 
        
        else:
            values = {"username": username, "password": password}

            return values
 

