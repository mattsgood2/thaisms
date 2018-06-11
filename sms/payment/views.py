from django.shortcuts import render

# Create your views here.
from django.core.urlresolvers import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
# from cart import Cart

def payment_process(request):
    menu_id = request.session.get('menu_id')
    menu = get_object_or_404(Menu, id=menu_id)

    paypal_dict = {
        "business": "receiver_email@example.com",
        "amount": "10000000.00",
        "item_name": "Menu {}".format(Menu.id),
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('your-return-view')),
        "cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"menu": menu, "form": form}
    return render(request, "cart/process.html", context)
