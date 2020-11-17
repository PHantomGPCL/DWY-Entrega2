from django import forms
from django.forms import ModelForm
from .models import List
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class RegistrarUsario(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-4'}),label="Nombre de Usuario")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control col-md-4'}), label="Correo")
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control col-md-4'}),label="Contraseña")
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control col-md-4'}),label="Confirmar contraseña")
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(forms.Form):
    usr=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-4'}),label="Nombre de Usuario")
    passwd=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control col-md-4'}),label="Contraseña")
