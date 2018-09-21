from django.urls import reverse
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
    carts = Cart(request)

    for price in carts:
        # print(price['quantity'])
        # print('your total quantity is {} and menu is {}, total is {}'.format(price['quantity'],price['menu'],price['total_price']))
        print('Your Order is {},'.format(price['menu']))
        # print(price)
        # def theloop(self):


    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": '%.2f' % carts.get_total_price(),
        "item_name": "{}" .format(price), #menu_id = str(menu.id)
        # "item_name": "{}" .format(price['menu']),
        "invoice": "unique-invoice-id",
        "currency_code": 'GBP',
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('payment:done')),
        "cancel_return": request.build_absolute_uri(reverse('payment:canceled')),
        # "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"price":price, "form": form}
    # print (cart)
    return render(request, 'payment/process.html', context)

    # C:\Users\Matt\Documents\thaisms\sms\payment\templates\payment\process.html
