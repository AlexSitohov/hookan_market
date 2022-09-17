from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(initial=1, max_value=40, min_value=1, widget=forms.NumberInput,
                                  label='Количество')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
