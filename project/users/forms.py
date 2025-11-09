from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    """Form to signing the user up"""
    username = forms.CharField(
        label='نام کاربری',
        help_text='نام کاربری می‌تواند شامل حروف، اعداد و کاراکترهای @/+/-/./_ باشد.',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'نام کاربری خود را وارد کنید',
        })
    )
    email = forms.EmailField(
        label='ایمیل',
        help_text='',
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'ایمیل خود را وارد کنید',
        })
    )
    password1 = forms.CharField(
        label='گذرواژه',
        help_text='گذرواژه باید دارای حداقل هشت کاراکتر و شامل اعداد و حروف باشد.',
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'گذرواژه خود را وارد کنید'
        })
    )
    password2 = forms.CharField(
        label='تکرار گذرواژه',
        help_text='',
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'گذرواژه را تکرار کنید',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    """Form to logging the user in"""
    username = forms.CharField(
        label='نام کاربری',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'نام کاربری خود را وارد کنید',
        })
    )
    password = forms.CharField(
        label='گذرواژه',
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'گذرواژه خود را وارد کنید',
        })
    )
