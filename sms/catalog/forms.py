from django import forms


class MenuAddToCartForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'size':'2', 'value':'1',
                                                                'class':'quantity','maxlength':'5'})
    error_message = {'invalid': 'Please enter a valid quantity'}, min_value=1)

    menu_slug = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(MenuAddToCartForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError("Cookies must be on")
        return self.cleaned_data
