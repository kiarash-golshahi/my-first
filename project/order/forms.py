from .models import Order
from django import forms

class OrderForm(forms.ModelForm):
    phone = forms.CharField(
        label='شماره تلفن',
        required=True,
        widget=forms.TextInput(attrs={
            'name': 'phone',
            'placeholder': 'شماره تلفن فعالی از خود وارد کنید',
        })
    )
    address = forms.CharField(
        label='نشانی',
        required=True,
        widget=forms.Textarea(attrs={
            'name': 'address',
            'placeholder': 'نشانی محل دریافت سفارش را وارد کنید',
        })
    )

    class Meta:
        model = Order
        fields = ['phone', 'address']
