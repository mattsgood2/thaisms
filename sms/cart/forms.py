from django import forms

MENU_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]

class CartAddMenuForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=MENU_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
