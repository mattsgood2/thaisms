from .models import CartItem
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import decimal
import random

def generate_cart_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ()1234567890!"£$%^&*()_+"'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0,len(characters)-1)]
        return cart_id

def get_cart_items(request):
    return CartItem.objects.filter(cart_id)

def add_to_cart(request):
    postdata = request.POST.copy()
    item_slug = postdata.get('menu_slug', '')
    quantity = postdata.get('quantity', '1')
    cart_products = get_cart_items(request)
    product_in_cart = False
    for cart_items in cart_products:
        if cart_items.menu.id == p.id:
            cart_items.adding_quantity(quantity)
            product_in_cart = True
    if not product_in_cart:
        ci = CartItem()
        ci.qauntity = qauntity
        ci.save()

def cart_count(request):
    return get_cart_items(request).count()
