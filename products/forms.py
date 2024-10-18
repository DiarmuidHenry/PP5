# products/forms.py

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'image', 'description', 'price', 'category', 'co2_footprint', 'stock', 'options']

    def clean_options(self):
        options = self.cleaned_data.get('options')
        if options is not None:  # Check if options is provided
            options_list = options.split(',')
            for option in options_list:
                if not option.strip():  # Check for empty options
                    raise ValidationError('Options cannot be empty.')
            return options  # Return the cleaned options
        return options  # Return None if options is not provided