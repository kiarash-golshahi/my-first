from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    """Form to signing the user up"""
    username = forms.CharField(
        label='نام کاربری',
        help_text='نام کاربری می‌تواند شامل حروف، اعداد و کاراکترهای @/+/-/./_ باشد.',
        required=True
    )
    email = forms.EmailField(
        label='ایمیل',
        help_text='',
        required=True
    )
    password1 = forms.CharField(
        label='گذرواژه',
        help_text='گذرواژه باید دارای حداقل هشت کاراکتر و شامل اعداد و حروف باشد.',
        required=True
    )
    password2 = forms.CharField(
        label='تکرار گذرواژه',
        help_text='',
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
