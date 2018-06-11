from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Menu
from .cart import Cart
from .forms import CartAddMenuForm

@require_POST
def cart_add(request, menu_id):
    cart = Cart(request)
    menu = get_object_or_404(Menu, id=menu_id)
    form = CartAddMenuForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(menu=menu, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, menu_id):
    cart = Cart(request)
    menu = get_object_or_404(Menu, id=menu_id)
    cart.remove(menu)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddMenuForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})

# from django.core.urlresolvers import reverse
# from django.shortcuts import render
# from paypal.standard.forms import PayPalPaymentsForm
#
#
# def payment_process(request):
#     menu_id = request.session.get('menu_id')
#     menu = get_object_or_404(Menu, id=menu_id)
#
#     paypal_dict = {
#         "business": "receiver_email@example.com",
#         "amount": "10000000.00",
#         "item_name": "Menu {}".format(Menu.id),
#         "invoice": "unique-invoice-id",
#         "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
#         "return": request.build_absolute_uri(reverse('your-return-view')),
#         "cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),
#         "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
#     }
#
#     # Create the instance.
#     form = PayPalPaymentsForm(initial=paypal_dict)
#     context = {"menu": menu, "form": form}
#     return render(request, "cart/process.html", context)
