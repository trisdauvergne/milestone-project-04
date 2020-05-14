from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name',
                  'email',
                  'phone_number',
                  'street_address_1',
                  'street_address_2',
                  'town',
                  'country',
                  'postcode')

    def __init__(self, *args, **kwargs):
        """ 
        Adding placeholders and classes, removing auto-generated
        labels and setting autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address_1': 'Address 1',
            'street_address_2': 'Address 2',
            'town': 'Town / City',
            'country': 'Country',
            'postcode': 'Postal Code',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
