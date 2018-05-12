from django.db import models
from django.urls import reverse

# Create your models here.
class Menu(models.Model):
    food_name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    old_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
    image = models.ImageField(blank=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    bestselling = models.BooleanField(default=False)
    meta_keywords = models.CharField("Meta Keywords", max_length=255)
    meta_description = models.CharField("Meta Keywords Description", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()

    class Meta:
        db_table = 'menu'
        ordering = ['food_name']
        verbose_name_plural = 'menu'


    def __str__(self):
        return ('Menu {0} {1}'.format(self.food_name, self.pk))


#############fix me as i know wrong but need to corret it ################
    def get_absolute_url(self):
        #return reverse('catalog:menu_detail', args=[str(self.id)])
        return reverse('catalog:menu_detail', kwargs={'slug': self.slug})
##########################################################################
#       'catalog.menu.views', {'catalog_slug': self.slug }
#        return reverse('view_reservation', args=[str(self.id)])
##########################################################################
    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None
