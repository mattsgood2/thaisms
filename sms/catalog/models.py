from django.db import models

# Create your models here.
class Menu(models.Model):
    food_name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    old_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
    image = models.ImageField()
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    bestselling = models.BooleanField(default=False)
    meta_keywords = models.CharField("Meta Keywords", max_length=255)
    meta_description = models.CharField("Meta Keywords", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()

    class Meta:
        db_table = 'menu'
        ordering = ['food_name']
        verbose_name_plural = 'menu'


    def __str__(self):
        return self.food_name

    def get_absolute_url(self):
        return ('catalog_menu', (), {'catalog_slug': self.slug })

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None
