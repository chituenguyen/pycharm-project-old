from django import forms
from django_countries.fields import CountryField


class CheckoutForm(forms.Form):
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '1234 Main'
    }))
    apartment = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Apartment or suite'
    }))
    country = CountryField(blank_label='(Select country)').formfield(widget=forms.Select(attrs={
        'class': 'custom-select d-block w-100'
    }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))


class CouponForm(forms.Form):
    code = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Promo code",
        'aria-label': "Recipient's username",
        'aria-describedby': "basic-addon2"
    }))


class RefundForm(forms.Form):
    code=forms.CharField(max_length=50)
    messages=forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email=forms.EmailField()
