from django import forms
from django.contrib.auth.models import User
from .models import CustomerProfile
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required= True)
    address = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField(max_length =15)

    class Meta:
        model = User 
        fields =['username','email','password1','password2','address','phone']