from decimal import Decimal
from django.conf import settings
from catalog.models import Menu


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, menu, quantity=1, update_quantity=False):
        menu_id = str(menu.id)
        if menu_id not in self.cart:
            self.cart[menu_id] = {'quantity': 0, 'price': str(menu.price)}
        if update_quantity:
            self.cart[menu_id]['quantity'] = quantity
        else:
            self.cart[menu_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self,menu):
        menu_id = str(menu.id)
        if menu_id in self.cart:
            del self.cart[menu_id]
            self.save()

    def __iter__(self):
        menu_ids = self.cart.keys()
        menus = Menu.objects.filter(id__in=menu_ids)
        for menu in menu:
            self.cart[str(menu.id)]['menu'] = menu

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
