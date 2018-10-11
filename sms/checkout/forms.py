from django import forms
# from checkout.models import YourAddress
# class GetAddress(forms.Form):
#     your_address = forms.CharField(label='Your Address', max_length=100)

class YourAddressForm(forms.Form):
    your_address = forms.CharField(label='Your Address', max_length=100)

    # class Meta:
    #     model = YourAddress
    #     fields = ['your_address', 'post_code',]
