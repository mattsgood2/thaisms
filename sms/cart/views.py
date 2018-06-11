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
    # return render(request, 'cart/detail.html', {'cart': cart})
    request.session['menu_id'] = menu.id
    return redirect(reverse('payment:process'))
