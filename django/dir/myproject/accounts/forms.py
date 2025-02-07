from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Account

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)#メールアドレスを必須にする例

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

# class UserLoginForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("username","email","password1","password2")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['profile_image']