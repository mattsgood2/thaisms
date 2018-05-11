from django.db import models
from sms.catalog.models import Menu
# Create your models here.


class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    menu_item = models.ForeignKey('catalog.Menu', unique=False)
