from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Menu
from cart.cart import Cart
from django.http import HttpResponseRedirect
from .forms import GetAddress

def get_address(request):
    cart = Cart(request)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        for item in cart:
        # create a form instance and populate it with data from the request:
            form = GetAddress(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GetAddress()

    return render(request, 'checkout/checkout.html', {'cart':cart, 'form': form})
