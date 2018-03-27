from django.db import models

# Create your models here.
class Menu(models.Model):
    food_name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords", max_length=255)
    meta_description = models.CharField("Meta Keywords", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = 'food_name'


    def __str__(self):
        return self.food_name

    def get_absolute_url(self):
        return ('catalog_menu', (), {'catalog_slug': self.slug })
