from django import forms

class GetAddress(forms.Form):
    your_address = forms.CharField(label='Your Address', max_length=100)
    
