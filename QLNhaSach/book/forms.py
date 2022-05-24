from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerInfo(ModelForm):
    class Meta:
        model = KhachHang
        fields = ['ho_ten', 'so_dien_thoai', 'email']
