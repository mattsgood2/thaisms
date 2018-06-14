from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Menu
from cart.cart import Cart
# from cart.views import cart_detail
# from django.views.generic.list import ListView


def checkout(request):
    cart = Cart(request)
    menu = get_object_or_404(Menu)
    # cart.remove(menu)
    return redirect('checkout:checkout')
# def checkout(request):
#     cart_detail = get_object_or_404(Cart)
#     for cart_details in cart_detail:
#     # menu = get_object_or_404(Menu, menu_id)
#         return render(request, 'checkout/checkout.html', {'cart_details': cart_details })


# def payment_process(request):
#     menu_id = request.session.get('menu_id')
#     menu = get_object_or_404(Menu, id=menu_id)
