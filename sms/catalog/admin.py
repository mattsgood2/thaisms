from django.contrib import admin
from .models import Menu
# Register your models here.
admin.site.register(Menu)


class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("food_name",)}
