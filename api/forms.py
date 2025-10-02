from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Product, Category

# Signup form
class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'mobile_no', 'email', 'role', 'password1', 'password2', 'photo']

# Login form
class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


# Edit profile form
class EditProfileForm(forms.ModelForm):
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter current password"}),
        required=False
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter new password"}),
        required=False
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Re-enter new password"}),
        required=False
    )

    class Meta:
        model = User
        fields = [
            "full_name", "mobile_no", "photo", "facebook_link",
            "security_question_1", "security_answer_1",
            "security_question_2", "security_answer_2"
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your full name"}),
            "mobile_no": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your mobile number"}),
            "photo": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "facebook_link": forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter your Facebook page link"}),
            "security_question_1": forms.TextInput(attrs={"class": "form-control", "placeholder": "E.g., What is your favorite book?"}),
            "security_answer_1": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your answer"}),
            "security_question_2": forms.TextInput(attrs={"class": "form-control", "placeholder": "E.g., What was the name of your first pet?"}),
            "security_answer_2": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your answer"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password or confirm_password:
            if new_password != confirm_password:
                raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


# Product form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'details', 'price', 'image', 'category']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter category description', 'rows': 2}),
        }
