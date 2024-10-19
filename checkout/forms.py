from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'name', 
            'email', 
            'phone_number', 
            'address_1', 
            'address_2', 
            'city', 
            'county', 
            'post_code', 
            'country'
        )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'address_1': 'Street Address 1',
            'address_2': 'Street Address 2',
            'city': 'Town or City',
            'county': 'County',
            'post_code': 'Postal Code',
            'country': 'Country',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
