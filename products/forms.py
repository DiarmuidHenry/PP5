from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'image', 'description', 'price', 'category', 'co2_footprint', 'stock', 'options']

    def clean_options(self):
        options = self.cleaned_data.get('options')
        if options:  # Only proceed if options is not None or an empty string
            options_list = options.split(',')
            for option in options_list:
                if not option.strip():  # Check for empty options
                    raise ValidationError('Options cannot contain empty values.')
            return options  # Return the cleaned options
        
        return ''