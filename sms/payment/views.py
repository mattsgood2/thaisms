from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from catalog.models import Menu
from cart.cart import Cart
from cart import cart
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings



@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')

@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')


def payment_process(request):
    cart = request.session.get(settings.CART_SESSION_ID)
    # menu = get_object_or_404(Menu)
    carts = Cart(request)
    for menu_id in cart:


    # for food_name in cart:
        # menu_id = menu
        # menu_id = menu.food_name
        # menu_id = get_object_or_404(Menu)
        # item = menu_food_name(pk=menu_id)
        # item['food_name']
        print(menu_id)
    # for item in menu_id:
    # for item in menu:
    #     item['food_name']
    # menu = get_object_or_404(Menu, menu_pk=settings.CART_SESSION_ID.pk)
    # for pk in settings.CART_SESSION_ID:
    #     menu.pk = settings.CART_SESSION_ID.pk
    #     return pk
        # print (cart)
        # print(item, pk=menu.food_name)

    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": '%.2f' % carts.get_total_price(),
        "item_name": "Menu {}" .format(cart), #menu_id = str(menu.id)
        "invoice": "unique-invoice-id",
        "currency_code": 'GBP',
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('payment:done')),
        "cancel_return": request.build_absolute_uri(reverse('payment:canceled')),
        # "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"cart":cart, "form": form}
    # print (cart)
    return render(request, 'payment/process.html', context)

    # C:\Users\Matt\Documents\thaisms\sms\payment\templates\payment\process.html
