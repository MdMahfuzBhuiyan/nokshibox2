from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Product

# Signup form
class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'mobile_no', 'email', 'role', 'password1', 'password2', 'photo']

# Login form
class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

# Product form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'details', 'price', 'image', 'category']