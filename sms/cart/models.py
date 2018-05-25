from django.db import models
# from catalog.models import Menu
# # Create your models here.
# class CartItem(models.Model):
#     cart_id = models.CharField(max_length=50)
#     date_added = models.DateTimeField(auto_now_add=True)
#     quantity = models.IntegerField(default=1)
#     menu = models.ForeignKey('catalog.Menu', unique=False)
#
#     class Meta:
#      db_table = 'cart_id'
#      ordering = ['date_added']
#
#     def total(self):
#          return self.quantity * self.menu.price
#
#     def name(self):
#         return self.food_name
#
#     def price(self):
#         return self.menu.price
#
#     def get_absolute_url(self):
#         return self.catalog.menu.get_absolute_url()
#
#     def augment_quantity(self, quantity):
#         self.quantity = self.quantity + int(quantity)
#
#         self.save()
