from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Menu
from cart.cart import Cart
from django.http import HttpResponseRedirect
from .forms import YourAddressForm

def get_address(request):
    cart = Cart(request)
    # if this is a POST request we need to process the form data
    # if request.method == 'POST':
        # for item in cart:
        # create a form instance and populate it with data from the request:
    form = YourAddressForm(request.POST)
        # check whether it's valid:
    if form.is_valid():
        # form.save()
        # text = form.cleaned_data['youraddress']
            # args = {'form': form, 'text':text}
        return redirect(reverse('payment:process'))
            # return render(request, 'payment:process', {'args': args})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = YourAddressForm()

        return render(request, 'checkout/checkout.html', {'cart':cart, 'form': form})
