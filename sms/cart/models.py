from django.db import models
from catalog.models import Menu
# Create your models here.


class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    menu_item = models.ForeignKey('catalog.Menu', unique=False)

    class Meta:
        db_table = 'cart_items'
        ordering = ['date_added']

    def total(self):
        return self.quantity *self.menu.price

    def name(self):
        return self.menu.name

    def price(self):
        return self.menu.price

    def get_absolute_url(self):
        return self.menu.get_absolute_url()

    def adding_quantity(self, quantity):
        self.quantity =self.quantity + int(quantity)
        self.save()
