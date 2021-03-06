from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# from .models import Order

# class OrderForm(ModelForm):
#     class Meta:
#         model =Order
#         fields = '__all__'

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email', 'password1', 'password2']
        