from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Menu
from cart.cart import Cart
# from cart.views import cart_detail
# from django.views.generic.list import ListView

from catalog.models import Menu
from django.http import HttpResponseRedirect
from django.shortcuts import render
from cart.cart import Cart
from .forms import GetAddress

def get_address(request):
    cart = Cart(request)
    # cart_show = str(cart)
    # menu = get_object_or_404(Menu, id=menu_id)
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
# def checkout(request):
#     cart = Cart(request)
#     menu = get_object_or_404(Menu)
#     # cart.remove(menu)
#     return redirect('checkout:checkout')
# def checkout(request):
#     cart_detail = get_object_or_404(Cart)
#     for cart_details in cart_detail:
#     # menu = get_object_or_404(Menu, menu_id)
#         return render(request, 'checkout/checkout.html', {'cart_details': cart_details })


# def payment_process(request):
#     menu_id = request.session.get('menu_id')
#     menu = get_object_or_404(Menu, id=menu_id)
